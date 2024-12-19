This is the original running lua script file : - Himanshu.
===========================================================

aman.gupta@ip-10-12-1-83:~/Scripts$ cat writeToDatabase.lua
print("Starting Lua script...")
function OnStableStudy(studyId, tags, metadata)
        local check = ParseJson(RestApiGet('/studies/'..studyId..'/instances'))
        local instanceTags = ParseJson(RestApiGet('/instances/'..check[1]["ID"]..'/simplified-tags'))


        local patientName = instanceTags["PatientName"]
        local patientAge = string.sub(instanceTags["PatientAge"], 2, 3)
        local patientGender = instanceTags["PatientSex"]
        local patientID = instanceTags["PatientID"]
        local studyDescription = instanceTags["StudyDescription"]
        local address = instanceTags["InstitutionAddress"]
        local studyDate = string.sub(instanceTags["StudyDate"], 7)..'-'..string.sub(instanceTags["StudyDate"], 5, 6)..'-'..string.sub(instanceTags["StudyDate"], 1, 4)
        local bodyPart = instanceTags["BodyPartExamined"]


        local command = 'python3 /usr/share/orthanc/Scripts/reportingbot.py "'..studyId..'" "'..patientName..'" "'..patientAge..'" "'..patientGender..'" "'..patientID..'" "'..studyDescription..'" "'..address..'" "'..studyDate..'" "'..bodyPart..'"'
        print("Executing command:", command)
        local handle = io.popen(command)
        local result = handle:read("*a")
        print(result)
end
aman.gupta@ip-10-12-1-83:~/Scripts$
