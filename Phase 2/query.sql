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

----------------------

SELECT "11-----------";
--List the video platform with the highest total views

SELECT video_platform
FROM
(
    SELECT video_platform, MAX(video_views)
    FROM video
    GROUP BY video_platform
);

----------------------

SELECT "12-----------";
--How many videos were produced by marketing team
--SOCIAL STARS and targets demographic "0 - 14 years"

SELECT COUNT(video_id)
FROM video, marketing, project, demographic
WHERE team_name = "SOCIAL STARS"
AND team_id = project_teamId
AND video_projectId = project_id
AND video_demographicId = demographic_id
AND demographic_name = "0 - 14 years";

----------------------

SELECT "13-----------";
--Regions who have not been requested by
--MCDONALDS or BURGER KING

SELECT region_name
FROM region
EXCLUDE
SELECT region_name
FROM region, request, reqregion, region
WHERE client_name = "MCDONALDS"
AND client_id  = request_clientId
AND request_id = rr_requestId
AND rr_regionId = region_id
EXCLUDE
SELECT r_regionName
FROM region, request, reqregion, region
WHERE client_name = "BURGER KING"
AND client_id  = request_clientId
AND request_id = rr_requestId
AND rr_regionId = region_id;

----------------------

SELECT "14-----------";
--Video with the lowest duration targeting females

SELECT video_id, video_file, MIN(video_duration)
FROM video, demographic
WHERE demographic_name = "FEMALE"
AND demographic_id = video_demographicId;

----------------------

SELECT "15-----------";
--Create a new project tied to marketing team 
--MAGIC INFLUENCERS working on request ID 8

INSERT INTO project(project_id, project_teamId,
                        project_requestId, project_cost) 
VALUES (100,4,8,0);

SELECT"NEW PROJECT"
SELECT * FROM project WHERE project_id = 100;

----------------------

SELECT "16-----------";
--Total projects made by marketing team TELEMARKETERS
SELECT COUNT(project_id)
FROM project, marketing
WHERE team_id = project_teamId
AND team_name = "TELEMARKETERS";

----------------------

SELECT "17-----------";
--Demographic with the highest views
SELECT demographic_name, MAX(total)
FROM
(
    SELECT demographic_name, SUM(video_views) as total
    FROM video, demographic
    WHERE video_demographicId = demographic_id
    GROUP BY demographic_id;
);

----------------------

SELECT "18-----------";
--Add middle school students to request 4
INSERT INTO reqDemo(rd_requestId, rd_demographicId) 
VALUES (8,4);

SELECT "CREATED CONNECTION WITH"
SELECT *
FROM reqDemo
WHERE rd_requestId = 8
AND rd_requestId = 4;

----------------------

SELECT "19-----------";
--Remove BIG TIME ADVERTS and all projects by them
SELECT "before DELETE"
SELECT *
FROM marketing
WHERE team_name = "BIG TIME ADVERTS";
SELECT *
FROM projects, marketing
WHERE team_id = project_teamId
AND team_name = "BIG TIME ADVERTS";

DELETE FROM projects,marketing
WHERE p_teamId = m_teamId
AND m_teamName = "BIG TIME ADVERTS";

DELETE FROM marketing
WHERE m_teamName = "BIG TIME ADVERTS";

SELECT "after DELETE"
SELECT *
FROM marketing
WHERE team_name = "BIG TIME ADVERTS";
SELECT *
FROM projects, marketing
WHERE team_id = project_teamId
AND team_name = "BIG TIME ADVERTS";

----------------------

SELECT "20-----------";
--Projects who don't cover all the requested regions
SELECT DISTINCT project_id
FROM
(
    SELECT rr_regionId, project_id
    FROM reqRegion, project
    WHERE rr_requestId = project_requestId
    EXCLUDE
    SELECT video_regionId, project_id
    FROM project, video
    WHERE video_projectId = project_id
);
