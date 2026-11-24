#!/bin/sh
# Run once from the repository root after copying the new files in.
# Removes the old Beautiful Jekyll template, which the new site no longer uses.
git rm -r -q --ignore-unmatch \
  index.md Gemfile.lock feed.xml Dockerfile LICENSE taurex.md \
  css js custom papers _plugins _bibliography \
  _layouts/base.html _layouts/post.html _layouts/minimal.html _layouts/tag_index.html _layouts/bibtemplate.html \
  _includes/footer-minimal.html _includes/social-share.html _includes/disqus.html _includes/navbarlink.html \
  _includes/footer-scripts.html _includes/head.html _includes/google_analytics.html _includes/nav.html \
  img/install-steps.gif img/404-southpark.jpg img/avatar-icon.png
git rm -q --ignore-unmatch CLEANUP.sh
echo "Old template removed. Review with: git status"
