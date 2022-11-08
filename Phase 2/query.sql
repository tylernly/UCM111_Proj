SELECT "1---------";
.headers off
--Select regions targeted by client Universal Studios
SELECT DISTINCT(region_name) 
FROM region, client, requests, reqRegion
WHERE client_name = 'UNIVERSAL STUDIOS'
AND client_id = request_clientId
AND request_id = rr_requestid
AND rr_regionid = region_id;


---------------------
SELECT "2---------";
--Select Client with the biggest request budget
SELECT client_name, max(request_budget)
FROM client, requests
WHERE client_id = request_clientid
AND request_budget = (SELECT max(request_budget) FROM requests)
GROUP BY client_name;

---------------------

SELECT "3---------";
--Total sum of duration for all videos made by team Social Stars
SELECT sum(video_duration)
FROM video, marketing, project
WHERE team_id = project_teamId
AND video_projectId = project_Id
AND team_name = 'SOCIAL STARS';

---------------------

SELECT "4---------";
--How many videos that target a region have the same language
SELECT region_name, COUNT(video_id)
FROM video, region
WHERE video_language = region_language
AND video_regionid = region_id
GROUP BY region_name;

----------------------

SELECT "5---------";
--Average amount of views for every video platform
SELECT video_platform, avg(video_views)
FROM video
GROUP BY video_platform;

----------------------

SELECT "6---------";
--Add a new video for project 2 that targets Europe and the language is Spanish
INSERT INTO video(video_id, video_file, video_duration,
                video_platform, video_views, video_regionId, 
                video_demographicId,video_projectId, video_cost, video_language)
VALUES('26','26','30','Google ADS','0','4','10','2','2000','Spanish');

SELECT DISTINCT(video_id), video_projectId, region_name, video_language
FROM video, region
WHERE video_id = 26    
AND region_id = video_regionId;

--------------------

SELECT "7----------";
--Find the the team with the most cost effective video being the ratio of (cost/views)
SELECT team_name, max(video_cost/video_views) * 1.0 as Effectiveness
FROM video, project , marketing
WHERE video_projectId = project_Id
AND project_teamId = team_Id
GROUP BY team_name
ORDER BY Effectiveness DESC
LIMIT 1;

---------------------

SELECT "8-----------";
--Delete projects where the cost went over the budget
DELETE FROM project
WHERE project_id in (SELECT project_id
                    FROM project, requests
                    WHERE project_cost > request_budget
                    AND project_requestId = request_Id);

SELECT * from project;

---------------------

SELECT "9------------";
--Change budget for request 15 to 5000
SELECT request_id, request_budget
FROM requests
WHERE request_id = 15;

UPDATE requests
SET request_budget = 5000
WHERE request_id = 15;

SELECT "Updated budget";
SELECT request_id, request_budget
FROM requests
WHERE request_id = 15;

---------------------

SELECT "10-----------";
--Change all client Id's for requests made by Universal Studios 
--to Marvel Studios

SELECT client_name, request_id, request_clientId
FROM requests, client
WHERE client_name = 'UNIVERSAL STUDIOS'
AND request_clientid = client_id;

UPDATE requests
SET request_clientId = 2
WHERE request_id = 1;

SELECT "Updated Requests";
SELECT client_name, request_id, request_clientId
FROM requests, client
WHERE client_name = 'MARVEL STUDIOS'
AND request_clientid = client_id;