# remove-bg-web
remove-bg is a website that removes the background from your photos, allowing more flexibility for you to choose whatever background you want!

# For Developers
## Required dependencies: 
- pipenv

## Getting Started
Run `pipenv install` at the root directory

To start the webapp, run 
`python manage.py runserver`
and navigate to [http://127.0.0.1:8000/webapp/index](http://127.0.0.1:8000/webapp/index)

## Docker Notes
To run it in docker, set the proper environment variables in `/env` and run 
`IMAGE=imagename &&
docker run --env-file env $IMAGE sh -c "python manage.py makemigrations && python manage.py migrate" &&
docker run --env-file env -p 80:8020 $IMAGE`




