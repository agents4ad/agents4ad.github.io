# agents4ad.github.io

This repo contains the source code for the homepage [https://agents4ad.github.io/](https://agents4ad.github.io/).

It's using [jekyll](https://jekyllrb.com/), see [https://jekyllrb.com/](https://jekyllrb.com/) for details on how to run it locally. If it's all set up locally, or when using the devcontainer, `$ bundle exec jekyll serve --livereload` does the job.

## Run locally with Docker

Start the site with the same Jekyll image used by this repo's devcontainer:

```bash
docker run --rm --network host -v "$PWD":/workspace -w /workspace mcr.microsoft.com/devcontainers/jekyll:0-bullseye bash -lc "bundle install && bundle exec jekyll serve --host 0.0.0.0 --port 4000 --livereload"
```

Then open [http://localhost:4000](http://localhost:4000).

## Workshop HTML5 slides

A standalone Reveal.js workshop deck is available at `slides/workshop-slides.html`.

- Open it directly in a browser: `file:///.../slides/workshop-slides.html`
- Or serve the site locally with Jekyll and open `http://localhost:4000/slides/workshop-slides.html`

## License

Unless otherwise stated, the source code in this repo is distributed under the 3-Clause BSD License, see [LICENSE](License).
