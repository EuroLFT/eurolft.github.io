#!/usr/bin/env python3


from argparse import ArgumentParser
from functools import cache
import re
import sys
from time import sleep

from qwikidata.sparql import return_sparql_query_results

import yaml


def read_yaml(filename):
    with open(filename, "r", encoding="utf-8") as yaml_file:
        return yaml.safe_load(yaml_file)


def get_only(candidates):
    if len(candidates) > 1:
        raise ValueError("Too many institutions found")
    elif len(candidates) == 1:
        return candidates.pop()
    else:
        return None


def get_existing_institution(domain, institutions):
    results = [
        institution
        for institution in institutions
        for match_domain in institution.get("match-domains")
        if domain.lower() == match_domain
        or domain.lower().endswith(f".{match_domain}")
    ]
    return get_only(results)


def get_existing_institution_by_name(name, institutions):
    results = [
        institution
        for institution in institutions
        if name == institution["name"]
    ]
    return get_only(results)


def is_academic_server(domain):
    non_academic_domains = [
        "fastmail.com",
        "gmail.com",
        "googlemail.com",
        "icloud.com",
        "outlook.com",
        "posteo.de",
    ]
    return not any(
        domain.lower().endswith(match_domain)
        for match_domain in non_academic_domains
    )


def build_backwards(domain):
    split_domain = domain.lstrip("@").split(".")
    for index in range(len(split_domain), 0, -1):
        yield ".".join(split_domain[index - 1:])


def safe_return_sparql_query_results(query):
    for attempt_index in range(1, 6):
        try:
            return return_sparql_query_results(query)
        except Exception as ex:
            print(
                f"SPARQL query failed with message {ex}; waiting {attempt_index} seconds"
            )
            sleep(attempt_index)

    raise RuntimeError("Can't connect to Wikidata")


@cache
def count_wikidata(domain):
    query = f"""
    SELECT (COUNT(DISTINCT ?institution) AS ?count)
    WHERE
    {{
    ?institution wdt:P31/wdt:P279* wd:Q3918; wdt:P856 ?website.
    SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }}
    FILTER(REGEX(STR(?website), "[/.]{domain}/")).
    }}
    """
    res = safe_return_sparql_query_results(query)
    return int(res["results"]["bindings"][0]["count"]["value"])


def suggest_sortkey(name):
    if name.startswith("Universi") or name.startswith("The "):
        result = re.match("[^A-Z]*([A-Z].*)", name[1:])
        if result:
            return suggest_sortkey(result.groups()[0])
        return name
    return name


def add_wikidata(data, domain):
    query = f"""
    SELECT DISTINCT ?institution ?institutionLabel ?website ?lon ?lat ?logo
    WHERE
    {{
    ?institution wdt:P31/wdt:P279* wd:Q3918; wdt:P856 ?website; wdt:P625 ?location; wdt:P154 ?logo.
    ?institution p:P625 ?coordinate.
    ?coordinate psv:P625 ?coordinate_node.
    ?coordinate_node wikibase:geoLongitude ?lon.
    ?coordinate_node wikibase:geoLatitude ?lat.
    SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }}
    FILTER(REGEX(STR(?website), "[/.]{domain}/")).
    }}
    """
    if domain not in data["match-domains"]:
        data["match-domains"].append(domain)

    results = safe_return_sparql_query_results(query)
    if len(results["results"]["bindings"]) == 0:
        print("No data returned.")
        return

    result = results["results"]["bindings"][0]
    data["name"] = result["institutionLabel"]["value"]
    data["sortkey"] = suggest_sortkey(data["name"])
    data["link"] = result["website"]["value"]
    data["image"] = result["logo"]["value"]
    data["lon"] = float(result["lon"]["value"])
    data["lat"] = float(result["lat"]["value"])


def get_institution_details(domain, institutions):
    print(f"{domain}:")
    if institution := get_existing_institution(domain, institutions):
        if "mailinglist" not in institution["categories"]:
            institution["categories"].append("mailinglist")
        print("We already know this one; skipping.")
        return

    if not is_academic_server(domain):
        print("This is a generic email alias; skipping.")
        return

    data = {
        "sortkey": None,
        "name": None,
        "link": None,
        "image": None,
        "lat": None,
        "lon": None,
        "categories": ["mailinglist"],
        "match-domains": [domain],
    }
    for partial_domain in build_backwards(domain):
        print(f"Trying {partial_domain}")
        match_count = count_wikidata(partial_domain)
        if match_count > 1:
            print("Too many matches, trying subdomain")
            continue
        if match_count == 1:
            print("Unique match found, trying to get data")
            try:
                wikidata = add_wikidata(data, partial_domain)
            except Exception as ex:
                print(f"Error occurred: {ex}")
            break
    else:
        print("No unique matches found; giving up.")

    print()

    return data


def get_args():
    parser = ArgumentParser()
    parser.add_argument("input_file", default=sys.stdin)
    parser.add_argument("--output_file", default=sys.stdout)
    parser.add_argument("--institution_file", default="_data/institutions.yml")
    parser.add_argument("--people_file", default="_data/members.yml")
    return parser.parse_args()


def main():
    args = get_args()

    people = read_yaml(args.people_file)
    institutions = read_yaml(args.institution_file)
    for institution in institutions:
        institution["categories"] = []

    # TODO: Replace with parsing of list export from GÉANT
    with open(args.input_file, "r", encoding="utf-8") as infile:
        for domain in infile:
            result = get_institution_details(domain.strip().lstrip("@"), institutions)
            if result:
                institutions.append(result)

    for person in people:
        if person["groups"]:
            institution = get_existing_institution_by_name(
                person["affiliation"], institutions
            )
            if institution is None:
                print(
                    f"{person['name']}'s affiliation ({person['affiliation']}) "
                    "is missing from the institution list."
                )
                continue

            if "board" not in institution["categories"]:
                institution["categories"].append("board")

    with open(args.output_file, "w", encoding="utf-8") as outfile:
        print(yaml.dump(institutions, sort_keys=False), file=outfile)


if __name__ == "__main__":
    main()
