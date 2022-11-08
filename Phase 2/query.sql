SELECT "1---------";
.headers off
--Select regions targeted by client Universal Studios
SELECT DISTINCT(r_regionname) 
FROM region, client, requests, reqRegion
WHERE c_clientname = 'UNIVERSAL STUDIOS'
AND c_clientid = r_requestclientId
AND r_requestid = rr_requestid
AND rr_regionid = r_regionid;

SELECT " ";

---------------------
SELECT "2---------";
--Select Client with the biggest request budget
SELECT c_clientname, max(r_requestbudget)
FROM client, requests
WHERE c_clientid = r_requestclientid
AND r_requestbudget = (SELECT max(r_requestbudget) FROM requests)
GROUP BY c_clientname;

SELECT " ";
---------------------

SELECT "3---------";
--Total sum of duration for all videos made by team Social Stars
SELECT sum(v_videoduration)
FROM video, marketing, project
WHERE m_teamid = p_teamId
AND v_videoprojectId = p_projectId
AND m_teamname = 'SOCIAL STARS';

SELECT " ";
---------------------

SELECT "4---------";
--How many videos that target a region have the same language as region
SELECT r_regionname, COUNT(v_videoid)
FROM video, region
WHERE v_videolanguage = r_regionlanguage
AND v_videoregionid = r_regionid
GROUP BY r_regionname;

SELECT " ";
----------------------

SELECT "5---------";
--Average amount of views for every video platform
SELECT v_videoplatform, avg(v_videoviews)
FROM video
GROUP BY v_videoplatform;

SELECT " ";
----------------------

SELECT "6---------";
--Add a new video for project 2 that targets Europe and the language is Spanish
SELECT DISTINCT(v_videoid), v_videoprojectId, r_regionname, v_videolanguage
FROM video, region
WHERE v_videoid = 26    
AND r_regionid = v_videoregionId;

INSERT INTO video(v_videoid, v_videofile, v_videoduration,
                v_videoplatform, v_videoviews, v_videoregionId, 
                v_videodemographicId,v_videoprojectId, v_videocost, v_videolanguage)
VALUES('26','26','30','Google ADS','0','4','10','2','2000','Spanish');

SELECT"Added new video for project 2"

SELECT DISTINCT(v_videoid), v_videoprojectId, r_regionname, v_videolanguage
FROM video, region
WHERE v_videoid = 26    
AND r_regionid = v_videoregionId;

SELECT " ";
--------------------

SELECT "7----------";
--Find the the team with the most cost effective video being the ratio of (cost/views)
SELECT m_teamname, max(v_videocost/v_videoviews) * 1.0 as Effectiveness
FROM video, project , marketing
WHERE v_videoprojectId = p_projectId
AND p_teamId = m_teamId
GROUP BY m_teamname
ORDER BY Effectiveness DESC
LIMIT 1;

SELECT " ";
---------------------

SELECT "8-----------";
--Delete projects where the cost went over the budget
--Project 3 and 6 should have been deleted
SELECT"Projects with cost over budget";
SELECT p_projectId, p_projectcost, r_requestId, r_requestBudget
FROM project, requests
WHERE p_projectcost > r_requestbudget
AND p_projectrequestId = r_requestId;

DELETE FROM project
WHERE p_projectid in (SELECT p_projectid
                    FROM project, requests
                    WHERE p_projectcost > r_requestbudget
                    AND p_projectrequestId = r_requestId);
SELECT"Removed projects with cost over budget";

SELECT p_projectId, p_projectcost, r_requestId, r_requestBudget 
FROM project, requests
WHERE p_projectrequestId = r_requestId;

SELECT " ";
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

SELECT " ";
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

SELECT " ";
-----------------------

SELECT "11-----------";
--Find the video platform with the highest total views
SELECT v_videoPlatform, videoSum
FROM (SELECT v_videoPlatform, SUM(v_videoViews) as videoSum from video
        GROUP BY v_videoPlatform) 
ORDER BY videoSum DESC  
LIMIT 1;

SELECT " ";
-----------------------

SELECT "12-----------";
--How many videos were produce by team Marketers that targeted Middle Schoolers
SELECT COUNT(v_videoId)
FROM video, marketing, project, demographic
WHERE m_teamName = 'MARKETERS'
AND m_teamID = p_teamId
AND v_videoProjectId = p_projectId
AND v_videoDemographicId = d_demographicId
AND d_demographicName = 'MIDDLE SCHOOL';

SELECT " ";
-------------------------

SELECT "13-----------";
--What regions have not been requested by M&M or Dove
SELECT DISTINCT(r_regionName)
FROM region
WHERE r_regionId not in (SELECT r_regionId 
                         FROM region, client, requests, reqregion
                         WHERE c_clientname = 'M&M'
                         AND r_requestid = rr_requestId
                         AND rr_regionId = r_regionId
                         AND c_clientId = r_requestclientId
                         UNION
                         SELECT r_regionId 
                         FROM region, client, requests, reqregion
                         WHERE c_clientname = 'DOVE'
                         AND r_requestid = rr_requestId
                         AND rr_regionId = r_regionId
                         AND c_clientId = r_requestclientId);

SELECT " ";
-------------------------

SELECT "14-----------";
--Video Id for lowest duration video targeting Male demographic 
SELECT v_videoId, v_videoFile, MIN(v_videoDuration)
FROM video, demographic
WHERE d_demographicname = 'MALE'
AND d_demographicId = v_videoDemographicId;

SELECT " ";
--------------------------

SELECT "15-----------";
SELECT m_teamname, p_projectid, p_projectrequestId
FROM requests, marketing, project
WHERE m_teamname = 'TELEMARKETERS'
AND p_teamId = m_teamId
AND p_projectrequestId = r_requestId;
--Create new project tied to team Telemarketers and request id 7
INSERT INTO project(p_projectid, p_teamId,
                    p_projectrequestId, p_projectcost) 
        VALUES (16,3,7,100000);
SELECT "Created new project for Telemarketers";

SELECT m_teamname, p_projectid, p_projectrequestId
FROM requests, marketing, project
WHERE m_teamname = 'TELEMARKETERS'
AND p_teamId = m_teamId
AND p_projectrequestId = r_requestId;

SELECT " ";
---------------------------

SELECT "16------------";
--Total projects created by marketing team Magic Influencers
SELECT m_teamName, COUNT(p_projectId)
FROM project, marketing
WHERE m_teamId = p_teamId
AND m_teamName = 'MAGIC INFLUENCERS';

SELECT " ";
---------------------------

SELECT "17-----------";
--Demographic name with video with highest views
SELECT d_demographicName, v_videoViews
FROM video, demographic
WHERE v_videoDemoGraphicId = d_demographicId
GROUP BY d_demographicId
ORDER BY max(v_videoViews) DESC
LIMIT 1;

SELECT " ";
----------------------------

SELECT "18-----------";
--Create new connection between demographic Male and request id 15
SELECT * FROM reqDemo WHERE rd_requestId = 15;
INSERT INTO reqDemo(rd_requestId, rd_demographicId) 
        VALUES (15,4);
SELECT "Updated Connection";
SELECT * FROM reqDemo WHERE rd_requestId = 15;

SELECT " ";
-----------------------------

SELECT "19-----------";
--Remove Marketing Team Big Time Adverts and projects by them
SELECT m_teamname, p_projectId
FROM project, marketing
WHERE p_teamId = m_teamId
AND m_teamname = 'BIG TIME ADVERTS';

DELETE FROM project
WHERE p_teamId = (SELECT m_teamId 
                FROM marketing 
                WHERE m_teamname = 'BIG TIME ADVERTS');
DELETE FROM marketing
WHERE m_teamname = 'BIG TIME ADVERTS';


SELECT "Deleted Big Time Adverts and projects";

SELECT m_teamname, p_projectId
FROM project, marketing
WHERE p_teamId = m_teamId
AND m_teamname = 'BIG TIME ADVERTS';

SELECT " ";
-------------------------

SELECT "20-----------";
--Find projects who's videos does not cover all the regions requested
SELECT DISTINCT p_projectId
FROM (SELECT rr_regionId, p_projectId
    FROM reqregion, project
    WHERE rr_requestId = p_projectrequestId
    EXCEPT
    SELECT v_videoRegionId, p_projectId
    FROM project, video
    WHERE v_videoProjectId = p_projectId
    ORDER BY p_projectId ASC);