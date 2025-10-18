# CI Pipeline Sample (Python Flask)

This repository is a ready-to-run sample for the assignment:
- GitHub Actions CI pipeline (build, test, docker build & push to GHCR)
- Dockerfile to containerize the app
- pytest test suite (5 tests)
- Jenkinsfile (declarative) showing equivalent pipeline stages

## Repository structure
```
ci-pipeline-sample-python/
├─ app/
│  ├─ app.py
│  └─ requirements.txt
├─ tests/
│  └─ test_app.py
├─ Dockerfile
├─ .github/workflows/ci.yml
├─ Jenkinsfile
└─ README.md
```

## Quick local setup & commands

1. Create and activate a Python virtualenv:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # on Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r app/requirements.txt
   ```

3. Run tests:
   ```bash
   pytest -q
   ```

4. Run the app locally:
   ```bash
   export FLASK_APP=app.app
   flask run --port=5000
   # or
   python -m app.app
   ```
   Open http://127.0.0.1:5000

5. Build Docker image locally:
   ```bash
   docker build -t ci-sample-python:local .
   docker run --rm -p 5000:5000 ci-sample-python:local
   ```

## GitHub Actions (CI)

The workflow is in `.github/workflows/ci.yml`. It:
- installs Python
- installs dependencies
- runs `pytest` (pipeline will fail if tests fail)
- builds a Docker image
- logs in to GitHub Container Registry (GHCR) and pushes the image

### Required repository secrets (for pushing to GHCR)
- `GITHUB_TOKEN` (provided automatically by GitHub Actions)
- No extra secrets are required to push to GHCR using `GITHUB_TOKEN`.
  If you want to push to Docker Hub, set `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` in repository secrets and update the workflow.

To demonstrate failure: intentionally change one test in `tests/test_app.py` to assert the wrong value, commit, and push — the workflow will fail.

## Jenkins

A `Jenkinsfile` is provided with equivalent stages. To run Jenkins locally (example using Docker):

```bash
docker run --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```

- Configure Docker credentials in Jenkins (Credentials -> Docker Registry) and set the ID used in the `Jenkinsfile`.
- Create a pipeline job pointing to this repo, or use webhooks to trigger.

## How to view CI results

- After pushing to GitHub, go to "Actions" tab in the repository to see workflow runs.
- The job will show test output and Docker build/push logs.

## Pull the Docker image (GHCR)

After workflow runs successfully the image will be at:
`ghcr.io/<OWNER>/<REPOSITORY>:v<run-number>` and `:latest`.

Pull example:
```bash
docker pull ghcr.io/OWNER/REPO:latest
```

## Notes
- Replace OWNER/REPO in the example above with your GitHub account and repository name.
- The CI workflow uses the repository `name` and `owner` to tag the image.

