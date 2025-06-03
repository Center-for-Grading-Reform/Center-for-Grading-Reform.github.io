---
layout              : page
show_meta           : false
title               : "The Grading Conference"
teaser              : ""
permalink           : "/grading-conference/abstracts/"
---
{% assign dates = "Null; Wednesday, June 11; Thursday, June 12; Friday, June 13" | split: "; "%}

- [Presentation Abstracts](#poster-abstracts) 
- [Poster Abstracts](#poster-abstracts) 


<h2>Presentation Abstracts</h2>
{% assign current_talks = site.data.twentytwentyfive.conference_talks | where: "year", 2025  | where: "format", "presentation" | sort: "title" %}
  {% for talk in  current_talks  %} 
    {% assign sessions = site.data.twentytwentyfive.conference_sessions | has: "parallel" %}
    {% for s in sessions %}
      {% for track in s.parallel %}
        {% if track.talks contains talk.abstract_id %}
          {% assign time = s.time %}
          {% assign day = s.day %}
          {% assign session_title = track.title %}
        {% endif %}
      {% endfor %}
    {% endfor %}
 <div id={{talk.abstract_id}}>
   <h4>{{ talk.title }}</h4>
   <p style="margin-bottom:0"><em>{{talk.authors | join: ", "}}</em></p>
   <b>{{session_title}}</b>
   {{ dates[day] | append: ", " | append: time | markdownify }}
   <p>{{talk.abstract | newline_to_br}} </p>

 </div>
 {% endfor %}
 
 <div id="poster-abstracts">
 <h2>Poster Abstracts</h2>
{% assign current_talks = site.data.twentytwentyfive.conference_talks | where: "year", 2025  | where: "format", "poster" | sort: "title" %}
 {% for talk in  current_talks  %} 
 <div id={{talk.abstract_id}}>
   <h4>{{ talk.title }} (#{{talk.abstract_id}})</h4>
   <p><em>{{talk.authors | join: ", "}}</em></p>
   <p>{{talk.abstract | newline_to_br}} </p>

 </div>
 {% endfor %}
 </div>