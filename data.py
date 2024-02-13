courses = [
    {
        "_id": "1",
        "code": "cs1",
        "description": "cs1des",
        "units": "3",
        "types": "labaratory"
    },
    {
        "_id": "2",
        "code": "cs2",
        "description": "cs2des",
        "units": "3",
        "types": "lecture"
    }
]

rooms = [
    {
        "_id": "1",
        "name": "room1",
        "types": "labaratory"
    },
    {
        "_id": "2",
        "name": "room2",
        "types": "lecture"
    }
]

students = [
    {
    "_id": "1",
    "program": "BSCS",
    "year": "4",
    "semester": "1",
    "block": "A",
    "courses": [
        {
            "code": "cs1",
            "description": "cs1des",
            "units": "3",
            "types": "labaratory"
        },
        {
            "_id": "2",
            "code": "cs2",
            "description": "cs2des",
            "units": "3",
            "types": "lecture"
        }
    ]
    },{
        "_id": "2",
        "program": "BSCS",
        "year": "2",
        "semester": "2",
        "block": "B",
        "courses": [
            {
                "code": "cs1",
                "description": "cs1des",
                "units": "3",
                "types": "labaratory"
            },
            {
                "_id": "2",
                "code": "cs2",
                "description": "cs2des",
                "units": "3",
                "types": "lecture"
            }
        ]
    }
]

teachers = [
    {
        "_id": "1",
        "name": "teacher1",
        "specialized": [
            {
                "_id": "1",
                "code": "cs1",
                "description": "cs1des",
                "units": "3",
                "types": "labaratory"
            },
            {
                "_id": "2",
                "code": "cs2",
                "description": "cs2des",
                "units": "3",
                "types": "lecture"
            }
        ]
    }
]