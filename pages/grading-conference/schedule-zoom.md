---
layout              : page-fullwidth
show_meta           : false
title               : "The Grading Conference"
teaser              : ""
permalink           : "/grading-conference/schedule-zoom/"
---
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<script type="text/javascript"> $(function(){ $(document).foundation() }); </script>
<script> var elem = new Foundation.Tabs(element, options); </script>

 Please note that all times are Eastern Daylight Time (UTC-4).

{% assign dates = "Wednesday, June 11; Thursday, June 12; Friday, June 13" | split: "; "%}
{% assign days = "1,2,3" | split: "," | to_i %}


<ul class="accordion" data-accordion style="margin-left: 0px">
{% for day in days %}
        {% assign ref = "day" | append: day %}
        {% assign href = "#" | append: ref %}
        <li class="accordion-navigation" >
        <a href="{{href}}">{{dates[forloop.index0]}}</a>

 <div id="{{ref}}" class="content">
<table class="schedule">

{% assign conference_day = site.data.twentytwentyfive.conference_sessions | where: "day", day  | sort: "slot" %}
{% for slot in conference_day %}
<tr>
  <td markdown="span" > {{slot.time}} </td>
  {%if slot.parallel %}
    {%for track in slot.parallel %}
     <td style="font-size: 1.05em">
        <b>{{track.title}}</b> {% if track.zoom %}(<a href="{{track.zoom}}">Zoom Link</a>)
        {% endif %}{% if track.slides-static %} (<a href="{{track.slides-static}}">Slides</a>){% endif %}
        <ul class="accordion" data-accordion style="margin-left: 0px">
        {% for id in track.talks %}
        {% assign talk = site.data.twentytwentyfive.conference_talks | where: "year", 2025 | find: "abstract_id", id %} 
        {% assign ref = "paper_" | append: id %}
        {% assign href = "#" | append: ref %}
        <li class="accordion-navigation" >
                <a href="{{href}}" style="font-size: 0.8em"> {{ talk.title }} </a> {% if talk.authors.size > 1 %} ({{talk.authors[0]}} et al.) {% elsif talk.authors.size == 1 %} ({{talk.authors[0]}})  {% endif %} 
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
  <td colspan="4" style="text-align: center; font-size:1.1em" >
    {% assign title = slot.title %}
    {% if slot.zoom %}
      {% assign title = title | append: " ([Zoom Link](" | append: slot.zoom | append: "))" %}
    {% endif %}
    {% if slot.slides-static %}
      {% assign title = title | append: " ([Slides](" | append: slot.slides | append: "))" %}
    {% endif %}
    {{ "**" | append: title | append: "**" | markdownify}}

    {% if slot.break %}
      <p>Join us in the <a href="https://calstatela.zoom.us/j/88153850073">Watercooler Zoom Room</a> to hang out and chat with fellow attendees.</p>
    {% endif %}

    {% if slot.poster-gallery %}
      <p>View the posters in the <a href="{{slot.poster-gallery}}">poster gallery</a> anytime, and then join the <a href="{{slot.zoom}}">Zoom room</a> at this time to chat with poster presenters.</p>
    {% endif %}

    {% if slot.keynote-title %}
      {% assign ref = "keynote" | append: slot.day %}
      {% assign href = "#" | append: ref %}
      <ul class="accordion" data-accordion="" style="margin-left: 0px">
        <li class="accordion-navigation" >
          <a href="{{href}}" style="font-size: 1em"> {{ slot.keynote-title }} </a> 
          <div id="{{ref}}" class="content">
          <p>{{slot.keynote-abstract | newline_to_br}}</p>
          </div>
          </li>
      </ul>
    {% endif %}
  </td>
     
  {% endif %}
</tr>
{% endfor %}
</table>
</div>
</li>
{% endfor %}
</ul>



