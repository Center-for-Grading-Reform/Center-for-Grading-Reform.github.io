---
layout              : page-fullwidth
show_meta           : false
title               : "The Grading Conference"
teaser              : ""
permalink           : "/grading-conference/schedule/"
---

All times Eastern

<table align="center">
<caption>Wednesday, June 11</caption>

<tr>
<td markdown="span">11:00 AM---12:00 PM EDT</td>
<td markdown="span" colspan="4">Welcome and Conference Orientation</td>
</tr>

<tr>
<td markdown="span">12:00 PM---1:00 PM EDT</td>
<td markdown="span" colspan="4">Keynote</td>
</tr>

<tr>
<td markdown="span">1:00 PM---2:00 PM EDT</td>
<td markdown="span" colspan="4">Meal Break</td>
</tr>

<tr>
<td markdown="span">2:00 PM---3:00 PM EDT</td>

{% for session in site.data.twentytwentyfive.conference_sessions %}
<td>
  <b>{{session.title}}</b>
  <ul class="accordion" data-accordion>
  {% for id in session.talks %}
    {% assign talk = site.data.twentytwentyfive.conference_talks | where: "year", 2025 | find: "abstract_id", id %} 
    {% assign ref = "paper_" | append: id %}
    {% assign href = "#" | append: ref %}
       <li class="accordion-navigation">
          <a href="{{href}}"> {{ talk.title }} </a> {% if talk.authors.size > 1 %} ({{talk.authors[0]}} et al.) {% else %} ({{talk.authors[0]}})  {% endif %} 
          <div id={{ref}} class="content">
            <p><em>{{talk.authors | join: ", "}}</em></p>
            <p>{{talk.abstract}}</p>
          </div>
        </li>
  {% endfor %}
  </ul>
</td>
{% endfor %}

<td>
Session 1.3C
        <ul>
        <li> {% assign id=73 %} 
        {% assign talk = site.data.twentytwentyfive.conference_talks | where: "year", 2025 | find: "abstract_id", id %} <a href="/grading-conference/abstracts/#{{id}}"> {{ talk.title }} </a> {% if talk.authors.size > 1 %} ({{talk.authors[0]}} et al.) {% else %} ({{talk.authors[0]}})  {% endif %} 
        </li>
        <li> {% assign id=53 %} 
        {% assign talk = site.data.twentytwentyfive.conference_talks | where: "year", 2025 | find: "abstract_id", id %} <a href="/grading-conference/abstracts/#{{id}}"> {{ talk.title }} </a> {% if talk.authors.size > 1 %} ({{talk.authors[0]}} et al.) {% else %} ({{talk.authors[0]}})  {% endif %} 
        </li>
        </ul>
</td>
<td>
Session 1.3D<br>
         {% assign id= 48 %} 
        {% assign talk = site.data.twentytwentyfive.conference_talks | where: "year", 2025 | find: "abstract_id", id %} <a href="/grading-conference/abstracts/#{{id}}"> {{ talk.title }} </a> {% if talk.authors.size > 1 %} ({{talk.authors[0]}} et al.) {% else %} ({{talk.authors[0]}})  {% endif %} 
</td>
</tr>

<tr>
<td markdown="span">3:00 PM---3:30 PM EDT</td>
<td markdown="span" colspan="4">Beverage Break</td>
</tr>

<tr>
<td markdown="span">3:30 PM---4:00 PM EDT</td>
<td>
Session 1.3A
        <ul>
        <li> Talk 1 </li>
        <li> Talk 2 </li>
        <li> Talk 3 </li>
        </ul>
</td>
<td>
Session 1.3B
        <ul>
        <li> Talk 1 </li>
        <li> Talk 2 </li>
        <li> Talk 3 </li>
        </ul>
</td>
<td>
Session 1.3C
        <ul>
        <li> Talk 1 </li>
        <li> Talk 2 </li>
        <li> Talk 3 </li>
        </ul>
</td>
<td>
Session 1.3D
</td>
</tr>

<tr>
<td markdown="span">4:30 PM---5:00 PM EDT</td>
<td markdown="span" colspan="4">Beverage Break</td>
</tr>

<tr>
<td markdown="span">5:00 PM---6:00 PM EDT</td>
<td>
Session 1.4A
        <ul>
        <li> Talk 1 </li>
        <li> Talk 2 </li>
        <li> Talk 3 </li>
        </ul>
</td>
<td>
Session 1.4B
        <ul>
        <li> Talk 1 </li>
        <li> Talk 2 </li>
        <li> Talk 3 </li>
        </ul>
</td>
<td>
Session 1.4C
        <ul>
        <li> Talk 1 </li>
        <li> Talk 2 </li>
        <li> Talk 3 </li>
        </ul>
</td>
<td>
Session 1.4D
</td>
</tr>

<tr>
<td markdown="span">6:00 PM---7:00 PM EDT</td>
<td markdown="span" colspan="4">Social Hour</td>
</tr>

</table>
