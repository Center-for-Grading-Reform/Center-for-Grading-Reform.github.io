---
layout              : page-fullwidth
show_meta           : false
title               : "The Grading Conference"
teaser              : ""
permalink           : "/grading-conference/schedule/"
---

All times Eastern

<table class="schedule">
<caption>Wednesday, June 11</caption>

{% assign day1 = site.data.twentytwentyfive.conference_sessions | where: "day", 1 %}
{% for slot in day1 %}
<tr>
  <td markdown="span" > {{slot.time}} </td>
  {%if slot.parallel %}
    {%for track in slot.parallel %}
     <td style="font-size: 1.05em">
        <b>{{track.title}}</b>
        <ul class="accordion" data-accordion style="margin-left: 0px">
        {% for id in track.talks %}
        {% assign talk = site.data.twentytwentyfive.conference_talks | where: "year", 2025 | find: "abstract_id", id %} 
        {% assign ref = "paper_" | append: id %}
        {% assign href = "#" | append: ref %}
        <li class="accordion-navigation" >
                <a href="{{href}}" style="font-size: 0.8em"> {{ talk.title }} </a> {% if talk.authors.size > 1 %} ({{talk.authors[0]}} et al.) {% else %} ({{talk.authors[0]}})  {% endif %} 
                <div id={{ref}} class="content">
                <p><em>{{talk.authors | join: ", "}}</em></p>
                <p>{{talk.abstract}}</p>
                </div>
                </li>
        {% endfor %}
        </ul>
      </td>
    {% endfor %}
  {% else %}
  <td markdown="span" colspan="4" style="text-align: center; font-size:1.1em" >**{{slot.title}}**</td>
  {% endif %}
</tr>
{% endfor %}


</table>
