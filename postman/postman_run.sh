#!/bin/bash

source "../.env"

postman login --with-api-key $POSTMAN_API
postman collection run $POSTMAN_COLLECTION -e $POSTMAN_ENV -n 200 --verbose
