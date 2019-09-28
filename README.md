# Intro

This site contains a set of essays about Software Engineering practices applied to the development of a Rock-Paper-Scissors game.

# TO-DO essays

1.  The Game and Versions
1.  First Draft
1.  Website Draft
1.  TDD
1.  Refactoring
1.  CI
1.  Design Patterns
1.  Git workflow
1.  Documentation?
1.  C/C++ lib binding?
1.  Agile Analysis and Design?
1.  Web-Based?
1.  AWS?
1.  REST API?
1.  Docker?
1.  Multi-player web-based?
1.  Machine Learning based?
1.  Continuous Delivery of Web-Based?

# Posts Index

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
