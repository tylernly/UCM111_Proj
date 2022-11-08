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

SELECT client_name, max(request_budget)
FROM client, requests
WHERE client_id = request_clientid
AND request_budget = (SELECT max(request_budget) FROM requests)
GROUP BY client_name;

---------------------

SELECT "3---------";

SELECT sum(video_duration)
FROM video, marketing, project
WHERE team_id = project_teamId
AND video_projectId = project_Id
AND team_name = 'SOCIAL STARS';

---------------------

SELECT "4---------";

SELECT COUNT(video_id)
FROM video, region
WHERE video_language = region_language
AND video_regionid = region_id;

----------------------

SELECT "5---------";

SELECT video_platform, avg(video_views)
FROM video
GROUP BY video_platform;

----------------------

SELECT "6---------";

INSERT INTO video(video_id, video_file, video_duration,
                video_platform, video_views, video_regionId, 
                video_demographicId, video_cost, video_language)
VALUES('26','26','30','Google ADS','0','4','10','2000','Spanish');

SELECT DISTINCT(region_name), video_language
FROM video, region
WHERE video_id = 26    
AND region_id = video_regionId;

--------------------

SELECT "7----------";

SELECT team_name, max(video_cost/video_views) * 1.0 as Effectiveness
FROM video, project , marketing
WHERE video_projectId = project_Id
AND project_teamId = team_Id
GROUP BY team_name
ORDER BY Effectiveness Desc
Limit 1;

---------------------

SELECT "8-----------";