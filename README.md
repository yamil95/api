# Raizen-API

to run Raizen API, using bash console:

Clone repo from GitHub:
``` bash
git clone https://github.com/PiConsulting/API-Raizen
cd API-Raizen 
```

Set permission to scripts:
``` bash
chmod +x scripts/**
```

Now you can use **virtualenv** or **docker** as next lines:

> - **Virtualenv**:
``` bash
 ./scripts/create_env.sh
./scripts/run.sh
```

> - **docker**:
``` bash
./scripts/build_docker.sh
./scripts/run.sh docker
```

Any way **Raizen-API** will be running on [http://localhost:5000]( http://localhost:8000 ).


For any problem, google it !
