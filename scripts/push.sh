#!/bin/sh

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_website_files() {
  git checkout --track origin/gh-pages
  git add . *.html
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git push --quiet "https://${GITHUB_TOKEN}@github.com/$BenjaSanchez/map-runs.git" gh-pages > /dev/null
  echo "Successfully updated map."
}

setup_git
commit_website_files
upload_files
