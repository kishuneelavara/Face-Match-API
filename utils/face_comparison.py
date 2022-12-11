import face_recognition


def verify_face(document_path,selfie_path):
    result={}

    print(document_path,selfie_path)
    try:
        known_image = face_recognition.load_image_file(document_path)
        unknown_image = face_recognition.load_image_file(selfie_path)

        biden_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([biden_encoding], unknown_encoding, 0.57)
        faceDis = face_recognition.face_distance([biden_encoding], unknown_encoding)
        print(results)

        print("Distance : ", faceDis)
        if faceDis[0] <= 0.57:
            result['faceResult'] = "Face Matched"
            print(result)
        else:
            result['faceResult'] = "Face Not Matched"
            print(result)

        return result
    except Exception as e:
        print(e)
        result['faceResult'] = "Face Not Found / something went wrong"
        print(result)
        return result
