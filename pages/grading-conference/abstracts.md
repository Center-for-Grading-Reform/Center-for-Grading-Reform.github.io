---
layout              : page
show_meta           : false
title               : "The Grading Conference"
teaser              : ""
permalink           : "/grading-conference/abstracts/"
---
{% assign dates = "Null; Tuesday, June 16; Wednesday, June 17; Thursday, June 18" | split: "; "%}

- [Presentation Abstracts](#poster-abstracts) 
- [Poster Abstracts](#poster-abstracts) 


<h2>Presentation Abstracts</h2>
{% assign current_talks = site.data.twentytwentysix.conference_talks |  where: "format", "presentation" | sort: "title" %}
  {% for talk in  current_talks  %} 
    {% assign sessions = site.data.twentytwentysix.conference_sessions | has: "parallel" %}
    {% assign time = "" %}
    {% assign day = "" %}
    {% assign session_title = "" %}
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
 <h4><a href="">View Poster Gallery</a></h4>
{% assign current_talks = site.data.twentytwentysix.conference_talks |  where: "format", "poster" | sort: "title" %}
 {% for talk in  current_talks  %} 
 <div id={{talk.abstract_id}}>
   <h4>{{ talk.title }} (#{{talk.abstract_id}})</h4>
   <p><em>{{talk.authors | join: ", "}}</em></p>
   <p>{{talk.abstract | newline_to_br}} </p>

 </div>
 {% endfor %}
 </div>