---
layout              : page-fullwidth
show_meta           : false
title               : "The Grading Conference"
teaser              : ""
permalink           : "/grading-conference/schedule/"
---
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<script type="text/javascript"> $(function(){ $(document).foundation() }); </script>
<script> var elem = new Foundation.Tabs(element, options); </script>

 Please note that all times are Eastern Daylight Time (UTC-4).

{% assign dates = "Tuesday, June 16; Wednesday, June 17; Thursday, June 18" | split: "; "%}
{% assign days = "1,2,3" | split: "," | to_i %}


<ul class="accordion" data-accordion style="margin-left: 0px">
{% for day in days %}
        {% assign ref = "day" | append: day %}
        {% assign href = "#" | append: ref %}
        <li class="accordion-navigation" >
        <a href="{{href}}">{{dates[forloop.index0]}}</a>

 <div id="{{ref}}" class="content">
<table class="schedule">

{% assign conference_day = site.data.twentytwentysix.conference_sessions | where: "day", day  | sort: "slot" %}
{% for slot in conference_day %}
<tr>
  <td markdown="span" > {{slot.time}} </td>
  {%if slot.parallel %}
    {%for track in slot.parallel %}
     <td style="font-size: 1.05em">
        {% assign track_letter = track.first.last %}
        <b>{{slot.slot}}{{track_letter}} {{track.title}}</b>
        <ul class="accordion" data-accordion style="margin-left: 0px">
        {% for id in track.talks %}
        {% assign talk = site.data.twentytwentysix.conference_talks  | find: "abstract_id", id %} 
        {% assign ref = "paper_" | append: id %}
        {% assign href = "#" | append: ref %}
        <li class="accordion-navigation" >
                <a href="{{href}}" style="font-size: 0.8em"> {{ talk.title }} </a> {% if talk.authors.size > 1 %} ({{talk.authors[0]}} et al.) {% elsif talk.authors.size == 1 %} ({{talk.authors[0]}})  {% endif %} 
                <div id={{ref}} class="content">
                <p><em>{{talk.authors | join: ", "}}</em>
                {% if talk.panelists.size > 0 %}<br><em>Panelists: {{talk.panelists | join: ", "}}</em>{% endif %}
                </p>

                <p>{{talk.abstract}}</p>
                </div>
                </li>
        {% endfor %}
        </ul>
      </td>
    {% endfor %}
  {% else %}
  <td colspan="4" style="text-align: center; font-size:1.1em" >
    {% if slot.title == "Break" or slot.title contains "Social Hour" %}
      {{"**" | append: slot.title | append: "**" | markdownify}}
    {% else %}
      {{"**" | append: slot.slot | append: " " | append: slot.title | append: "**" | markdownify}}
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



