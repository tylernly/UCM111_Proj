def insert_marketing(_conn, _id, _name):
    try:
        sql = """INSERT INTO marketing(m_teamId, m_teamName) 
        VALUES (?,?);"""
        args = [_id, _name]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_requests(_conn, _id, _clientId, _budget):
    try:
        sql = """INSERT INTO requests(r_requestId, r_requestClientId, r_requestBudget) 
        VALUES (?,?,?);"""
        args = [_id, _clientId, _budget]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_project(_conn, _id, _teamId, _requestId, _cost):
    try:
        sql = """INSERT INTO project(p_projectId, p_projectTeamId,
                                p_projectRequestId, p_projectCost) 
        VALUES (?,?,?,?);"""
        args = [_id, _teamId, _requestId, _cost]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_video(_conn, _id, _file, _duration, _platform, _views,
                _language, _cost, _regionId, _demographicId, _projectId):
    try:
        sql = """INSERT INTO video(v_videoId, v_videoFile, v_videoDuration,
                                   v_videoPlatform, v_videoViews, v_videoLanguage,
                                   v_videoCost, v_videoRegionId, v_videoDemographicId
                                   v_projectId) 
        VALUES (?,?,?,?,?,?,?,?,?,?);"""
        args = [_id, _file, _duration, _platform, _views,
                _language, _cost, _regionId, _demographicId, _projectId]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_region(_conn, _id, _name, _language):
    try:
        sql = """INSERT INTO region(reigon_id, region_name, region_language) 
        VALUES (?,?,?);"""
        args = [_id, _name, _language]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)


def insert_demographic(_conn, _id, _name):
    try:
        sql = """INSERT INTO demographic(d_demographicId, d_demographicName) 
        VALUES (?,?);"""
        args = [_id, _name]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_reqDemo(_conn, _requestId, _demographicId):
    try:
        sql = """INSERT INTO reqDemo(rd_requestId, rd_demographicId) 
        VALUES (?,?);"""
        args = [_requestId, _demographicId]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_reqRegion(_conn, _requestId, _regionId):
    try:
        sql = """INSERT INTO reqRegion(rr_requestId, rr_regionId) 
        VALUES (?,?);"""
        args = [_requestId, _regionId]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def update_client(_conn, _id, _name):
    try:
        sql = """UPDATE client SET c_clientName = ? WHERE c_client_id = ?;"""
        args = [_name,_id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def update_marketing(_conn, _id, _name):
    try:
        sql = """UPDATE marketing SET m_marketingName = ? WHERE m_marketingId = ?;"""
        args = [_name, _id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def update_requests(_conn, _id, _clientId, _budget):
    try:
        sql = """UPDATE requests SET request_clientId = ?, request_budget = ? WHERE request_id = ?;"""
        args = [_clientId, _budget, _id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def update_project(_conn, _id, _teamId, _requestId, _cost):
    try:
        sql = """UPDATE project SET project_teamId = ?,
                 project_requestId = ?, project_cost = ? WHERE project_id = ?;"""
        args = [_teamId, _requestId, _cost, _id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_video(_conn, _id, _file, _duration, _platform, _views,
                _language, _cost, _regionId, _demographicId):
    try:
        sql = """UPDATE video SET video_file = ?, video_duration = ?,
                                   video_platform = ?, video_views = ?, video_language = ?,
                                   video_cost = ?, video_regionId = ?, video_demographicId = ?
                              WHERE video_id = ?;"""
        args = [_file, _duration, _platform, _views,
                _language, _cost, _regionId, _demographicId, _id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def update_region(_conn, _id, _name, _language):
    try:
        sql = """UPDATE region SET region_name = ?, region_language = ? WHERE reigon_id = ?;"""
        args = [_name, _language, _id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)


def update_demographic(_conn, _id, _name):
    try:
        sql = """UPDATE demographic SET demographic_name = ? WHERE demographic_id = ?;""" 
        args = [_name, _id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def update_reqRegion(_conn, _requestId, _regionId, new_requestId, new_regionId):
    try:
        sql = """UPDATE reqREgion SET rd_requestId = ?, rd_regionId = ?
        WHERE rd_requestId = ? AND rd_regionId;"""
        args = [new_requestId, new_regionId, _requestId, _regionId]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def update_reqDemo(_conn, _requestId, _demographicId, new_requestId, new_demographicId):
    try:
        sql = """UPDATE reqDemo SET rd_requestId = ?, rd_demographicId = ?
        WHERE rd_requestId = ? AND rd_demographicId;"""
        args = [new_requestId,new_demographicId, _requestId, _demographicId]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def delete_client(_conn, _id):
    try:
        sql = """DELETE FROM client WHERE client_id = ?;"""
        args = [_id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def delete_marketing(_conn, _id):
    try:
        sql = """DELETE FROM marketing WHERE marketing_id =?;"""
        args = [_id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def delete_requests(_conn, _id):
    try:
        sql = """DELETE FROM requests WHERE request_id = ?;""" 
        args = [_id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def delete_project(_conn, _id):
    try:
        sql = """DELETE FROM project WHERE project_id = ?;"""
        args = [_id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def delete_video(_conn, _id):
    try:
        sql = """DELETE FROM video WHERE video_id = ?;""" 
        args = [_id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def delete_region(_conn, _id):
    try:
        sql = """DELETE FROM region WHERE reigon_id = ?;"""
        args = [_id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)


def delete_demographic(_conn, _id):
    try:
        sql = """DELETE FROM demographic WHERE demographic_id = ?;"""
        args = [_id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def delete_reqDemo(_conn, _requestId, _demographicId):
    try:
        sql = """DELETE FROM reqDemo WHERE rd_requestId = ? AND rd_demographicId = ?;""" 
        args = [_requestId, _demographicId]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def delete_reqRegion(_conn, _requestId, _regionId):
    try:
        sql = """DELETE FROM reqRegion WHERE rr_requestId = ? AND rr_regionId = ?;"""
        args = [_requestId, _regionId]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)