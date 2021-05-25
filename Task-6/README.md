# Show Advertisements Per User
## Getting Started
The service is based on `dockers`, two images are required,
one for Mysql and one for python app.

### Usage
- Port `3306` and `8080` are required by Docker, make sure they are not occupied.
- Run the following command to start the app. Export of data will start once
  MySQL dB is up, it will take a while to dump data,
  and upon completing the export, the Flask server will start.
     ```sh
     $ make run 
     ```
- Run following command to check the status.
     ```sh
     $ make status 
     ```
- To stop the containers:
     ```sh
     $ make stop 
     ```
---

## API Documentation

 Provides advertisement seen per user API,
 returns the amount of advertisements the user has seen.

 **URL** : `/ads/user/<userid>`

**Method** : `GET`
## Success Response

**Code** : `200 OK`

**Content examples**

For a User with ID 6096033656594890947 on the local database where that User has saved
advertisement data

```json
{
    "seen_ads": [
        38
    ]
}
```

**Curl**

```sh
$ curl http://localhost:8080/ads/user/6096033656594890947
```


## Notes

* If the User does not have any instance 0 would be returned.