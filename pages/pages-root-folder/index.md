---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: frontpage
header:
  image_fullwidth: landscape-header.jpg
widget1:
  title: "Conferences"
  url: '/conferences/'
  image: virtual-conference.jpg
  text: 'The flagship program of our center is the annual Grading Conference, held virtually each June.'
widget2:
  title: "Resources"
  url: '/resources/'
  text: 'Browse our collection of resources for alternative grading practitioners'
  image: 'resources.jpg'
widget3:
  title: "About"
  url: '/about/'
  image: 'about.jpg'
  text: 'Learn more about who we are and the work that we do.'
#
# Use the call for action to show a button on the frontpage
#
# To make internal links, just use a permalink like this
# url: /getting-started/
#
# To style the button in different colors, use no value
# to use the main color or success, alert or secondary.
# To change colors see sass/_01_settings_colors.scss
#
#callforaction:
#  url: https://tinyletter.com/feeling-responsive
#  text: Inform me about new updates and features ›
#  style: alert

permalink: /index.html
#
# This is a nasty hack to make the navigation highlight
# this page as active in the topbar navigation
#
homepage: true
---

<!-- Things here show up above the widgets on the frontpage -->

&nbsp;  

The Center for Grading Reform seeks to advance education in the United States by supporting effective grading reform at all levels through conferences, educational workshops, professional development, research and scholarship, influencing public policy, and community building.
<!--more-->

<!-- This shows up below widgets and callforaction button -->

