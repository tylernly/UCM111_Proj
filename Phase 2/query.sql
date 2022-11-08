SELECT "1---------";
.headers off

SELECT DISTINCT(region_name) 
FROM region, client, requests, reqRegion
WHERE client_name = "UNIVERSAL STUDIOS"
AND client_id = request_clientId
AND request_id = rr_requestid
AND rr_regionid = region_id;


---------------------
SELECT "2---------";

SELECT client_name, min(request_budget)
FROM client, requests
WHERE client_id = request_clientid
AND request_budget = (SELECT min(request_budget) FROM requests)
GROUP BY client_name;

---------------------

SELECT "3---------";

SELECT sum(video_duration)
FROM video, marketing, project
WHERE team_id = project_teamId
AND video_projectId = project_Id
AND team_name = 'SOCIAL STARS';
