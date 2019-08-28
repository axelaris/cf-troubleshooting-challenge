# Moderate 05
Moderate tasks covers more complicated topics and complex issues,
or demands some CloudFoundry deeper knowledge, like routing or
healthchecks. 

## Application:
This is static golang web application, showing html page 

##Task:
Deploy and run application on CloudFoundry, using `cf push`
command and manifest. We expect main properties beeing configured
in manifest. Here we expect, that nothing deleted from manifest, but
properties can be added. 

NOTE: `cf push` can be sucsessfull, but please make sure that the app is working

##Expected result
app is shown in browser. `cf logs` is shown. `cf a` is shown

## Tags
`cf push` `manifest` `routes`
