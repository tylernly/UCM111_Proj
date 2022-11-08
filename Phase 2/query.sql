SELECT "1---------";
.headers off
--Select regions targeted by client Universal Studios
SELECT DISTINCT(r_regionname) 
FROM region, client, requests, reqRegion
WHERE c_clientname = 'UNIVERSAL STUDIOS'
AND c_clientid = r_requestclientId
AND r_requestid = rr_requestid
AND rr_regionid = r_regionid;


---------------------
SELECT "2---------";
--Select Client with the biggest request budget
SELECT c_clientname, max(r_requestbudget)
FROM client, requests
WHERE c_clientid = r_requestclientid
AND r_requestbudget = (SELECT max(r_requestbudget) FROM requests)
GROUP BY c_clientname;

---------------------

SELECT "3---------";
--Total sum of duration for all videos made by team Social Stars
SELECT sum(v_videoduration)
FROM video, marketing, project
WHERE t_teamid = p_projectteamId
AND v_videoprojectId = p_projectId
AND t_teamname = 'SOCIAL STARS';

---------------------

SELECT "4---------";
--How many videos that target a region have the same language
SELECT r_regionname, COUNT(v_videoid)
FROM video, region
WHERE v_videolanguage = r_regionlanguage
AND v_videoregionid = r_regionid
GROUP BY r_regionname;

----------------------

SELECT "5---------";
--Average amount of views for every video platform
SELECT v_videoplatform, avg(v_videoviews)
FROM video
GROUP BY v_videoplatform;

----------------------

SELECT "6---------";
--Add a new video for project 2 that targets Europe and the language is Spanish
INSERT INTO video(v_videoid, v_videofile, v_videoduration,
                v_videoplatform, v_videoviews, v_videoregionId, 
                v_videodemographicId,v_videoprojectId, v_videocost, v_videolanguage)
VALUES('26','26','30','Google ADS','0','4','10','2','2000','Spanish');

SELECT DISTINCT(v_videoid), v_videoprojectId, r_regionname, v_videolanguage
FROM video, region
WHERE v_videoid = 26    
AND r_regionid = v_videoregionId;

--------------------

SELECT "7----------";
--Find the the team with the most cost effective video being the ratio of (cost/views)
SELECT t_teamname, max(v_videocost/v_videoviews) * 1.0 as Effectiveness
FROM video, project , marketing
WHERE v_videoprojectId = p_projectId
AND p_projectteamId = t_teamId
GROUP BY t_teamname
ORDER BY Effectiveness DESC
LIMIT 1;

---------------------

SELECT "8-----------";
--Delete projects where the cost went over the budget
DELETE FROM project
WHERE p_projectid in (SELECT p_projectid
                    FROM project, requests
                    WHERE p_projectcost > r_requestbudget
                    AND p_projectrequestId = r_requestId);

SELECT * from project;

---------------------

SELECT "9------------";
--Change budget for request 15 to 5000
SELECT r_requestid, r_requestbudget
FROM requests
WHERE r_requestid = 15;

UPDATE requests
SET r_requestbudget = 5000
WHERE r_requestid = 15;

SELECT "Updated budget";
SELECT r_requestid, r_requestbudget
FROM requests
WHERE r_requestid = 15;

---------------------

SELECT "10-----------";
--Change all client Id's for requests made by Universal Studios 
--to Marvel Studios

SELECT c_clientname, r_requestid, r_requestclientId
FROM requests, client
WHERE c_clientname = 'UNIVERSAL STUDIOS'
AND r_requestclientid = c_clientid;

UPDATE requests
SET r_requestclientId = 2
WHERE r_requestid = 1;

SELECT "Updated Requests";
SELECT c_clientname, r_requestid, r_requestclientId
FROM requests, client
WHERE c_clientname = 'MARVEL STUDIOS'
AND r_requestclientid = c_clientid;