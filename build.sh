docker build -t 4d_johoshori ./
docker create --name 4d_johoshori -v `pwd`:/env -it 4d_johoshori /bin/bash