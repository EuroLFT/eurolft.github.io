# eurolft.github.io

The EuroLFT website

## Submitting announcements

All are welcome to submit announcements to the website.

1. Fork this repository
2. Add a new file in the `_announcements` directory
   named with the pattern `202Y-MM-DD-short-title.md`
   with the form:

   ~~~
   ---
   layout: post
   title: "Your Announcement Title Here"
   subtitle: "Optional subtitle for the title; otherwise remove this line."
   date: 202Y-MM-DD HH:MM +TZTZ
   ---
   
   Add any text you want to display in the detailed announcement here.
   This can make use of Markdown formatting;
   for more details on this,
   see
   [the Kramdown reference](https://kramdown.gettalong.org/quickref.html).
   ~~~

   Replace `Y`, `MM`, `DD`, `HH`, `MM`, and `+TZTZ` with
   the numeric year, month, day, hour, minute, and time zone of your post.
   For example,
   11PM on the 24th September 2025 in the UK
   (British Summer Time)
   would be 2025-09-24 23:00 +0100.
3. Make a pull request to this repository.
   (See [GitHub's documentation on this][gh-pr])

## For EuroLFT members

Similarly to the above,
changes may be made in a fork and pull requested.

### Adding events

Adding events can be done in a similar way to announcements,
but using the `_events` directory,
and with a format like:

~~~
---
layout: post
title: "Event title"
date: 202Y-MM-DD HH:MM +TZTZ
textdate: "202Y-MM-DD"
location: "Event location"
---

Event description text here.
~~~

`textdate` should be the plain text to display for when the event is taking place,
and may for example indicate a date range.

After an event takes place,
it should be moved to the `_past_events` directory,
so that it shows up in the correct section.

### Adding people

People are listed in `_data/members.yml`;
each has the form

~~~
- name: "Member Name"
  affiliation: "Institution Name"
  institution-url: "https://path-to-institution.tld"
  groups:
   - any
   - groups
   - member
   - is
   - in
  image: image_basename
  orcid: "XXXX-XXXX-XXXX-XXXX"
  pronouns: "insert/here"
~~~

- `groups` may contain committees or working groups,
  or any other grouping.
- `image` is optional;
  if missing,
  a generic headshot icon will be displayed instead.
  If present,
  this must be the base name of a `.jpg` file located in `/img/members/`.
  For example,
  `image: kenwilson`
  would look for the file `/img/members/kenwilson.jpg`.
- `orcid` is optional;
  if missing
  no ORCID icon/link will be displayed.
- `pronouns` is optional;
 if missing,
 no pronouns will be displayed.

### Adding groups

While any number of groups can be added to `_data/_members.yml`,
they only show up on the built website if they are listed in `_data/member_groups.yml`.

Each group has the form:

~~~
- shortname: easy_handle_matching_members_yml
  fullname: "Full Display Name of Group"
  description: "Longer description of what the group does goes here."
~~~

Note that the value of `shortname`
should match the value added to the `groups` list in `_data/members.yml_`.

### Adding institutions

To add member institutions to the list and map,
add a block to `_data/institutions.yml` of the form:

~~~
- name: "Name by which institution should be sorted"
  text: "Text to display for institution name"
  link: "https://path-to-institution.tld"
  image: logo_filename.extension
  lat: YY.YYYYY
  lon: XX.XXXXX
~~~

Note that:

- `name` allows a non-default sort order.
  For example,
  setting it to `Bonn` would avoid placing
  Universität Bonn
  between Swansea University and Universität Wuppertal.
- `image` should match a file placed in `img/institutions/`.
  In this case,
  unlike for people,
  the extension is required;
  SVG format is preferred,
  and high-resolution transparent PNG should SVG not be possible.
- `lat` and `lon` must be in decimal degrees;
  they will determine the position of the map pin.

For long words in institution names,
since the box that they fit in is small,
you may add a soft hyphen `&shy;` at points where hyphenation would be preferred.
For example,
`Forschungs&shy;zentrum`
may display as

```
Forschungs-
zentrum
```

rather than crashing off the right side of the box.

### Other pages

The following files are potentially interesting:

- `_config.yml`: Main site configuration
- `contact.md`: Contact page
- `index.html`: Main page
- `lft.md`: About LFT page
- `people/index.html`: Layout template for people and institution lists
- `people/governance.html`: Currently-unlinked governance structure page
- `people/map.html`: Institution map
- `announcements/index.html`, `events/index.html`, `events/past/index.html`:
  nominal index pages for announcements, events, and past events.
  Due to Jekyll bugs,
  these are largely blank,
  and the actual layouts for these pages are instead in
  `_layouts/announcements.html`,
  `_layouts/events.html`,
  and `_layouts/past_events.html`.

## Testing

The site is built with [Jekyll][jekyll],
which is a static site generator written in [Ruby][ruby].

To test,
it should be sufficient to:

1. Ensure that you have a recent version of Ruby installed
2. Clone the repository, and `cd` into it
3. Run

   ~~~
   bundle install
   ~~~

   This only needs to be done once,
   to install the required packages.
   
4. Run

   ~~~
   bundle exec jekyll serve
   ~~~
   
   to build the site and start a local server.
   This will print out a link to point your browser to to test;
   it is likely `http://localhost:4000`.

## Credits

The theme of this site is based on
the [Start Bootstrap Clean Blog Jekyll template][startbootstrap].

[gh-pr]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
[jekyll]: https://jekyllrb.com
[ruby]: https://www.ruby-lang.org/en/
[startbootstrap]: https://github.com/StartBootstrap/startbootstrap-clean-blog-jekyll
