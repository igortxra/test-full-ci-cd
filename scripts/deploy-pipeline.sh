#!/bin/bash

if [ "$GCP_CREDENTIALS" = "HOMOLOGATION" ]; then
    echo "Deploy será feito em staging"
else
    echo "Deploy será feito em development"
fi

echo "Versão a ser implantada: $VERSION"
