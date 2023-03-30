#!/bin/bash
# PUT METHOD is allowed, we must follow redirections, AlxAfrica and our userid should be user_id = 98
curl -sLX PUT -H "origin: AlxAfrica" -d "user_id=98" 0.0.0.0:5000/catch_me
