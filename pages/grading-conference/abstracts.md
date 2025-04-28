---
layout              : page
show_meta           : false
title               : "The Grading Conference"
teaser              : ""
permalink           : "/grading-conference/abstracts/"
---

<h2>Presentation Abstracts</h2>
{% assign current_talks = site.data.twentytwentyfive.conference_talks | where: "year", 2025  | where: "format", "presentation" | sort: "title" %}
 {% for talk in  current_talks  %} 
 <div id={{talk.abstract_id}}>
   <h4>{{ talk.title }}</h4>
   <p>{{talk.authors | join: ", "}}</p>
   <p>{{talk.abstract | newline_to_br}} </p>

 </div>
 {% endfor %}
 
 <h2>Poster Abstracts</h2>
{% assign current_talks = site.data.twentytwentyfive.conference_talks | where: "year", 2025  | where: "format", "poster" | sort: "title" %}
 {% for talk in  current_talks  %} 
 <div id={{talk.abstract_id}}>
   <h4>{{ talk.title }}</h4>
   <p>{{talk.authors | join: ", "}}</p>
   <p>{{talk.abstract | newline_to_br}} </p>

 </div>
 {% endfor %}