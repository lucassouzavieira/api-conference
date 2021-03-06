from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def schedule():
    response = {
        "schedule": [
            {
                "dia": "1",
                "mes": "mar",
                "grupos": [{
                    "horario": "8:00 am",
                    "sessoes": [{
                        "nome": "Breakfast",
                        "inicio": "8:00 am",
                        "termino": "9:00 am",
                        "local": "Main hallway",
                        "tag": "Food",
                        "id": "1"
                    }]
                }, {
                    "horario": "9:00 am",
                    "sessoes": [{
                        "nome": "Introduction to Appcamp.io",
                        "local": "Room 2203",
                        "descricao": "Descrição",
                        "palestrantes": ["Ellie Elephant"],
                        "inicio": "9:15 am",
                        "termino": "9:30 am",
                        "tag": "Ionic",
                        "id": "2"
                    }, {
                        "nome": "Getting started with Ionic",
                        "local": "Room 2202",
                        "descricao": "Descrição",
                        "palestrantes": ["Ted Turtle"],
                        "inicio": "9:30 am",
                        "termino": "9:45 am",
                        "tag": "Ionic",
                        "id": "3"
                    }]
                }]
            },
            {
                "dia": "2",
                "mes": "mar",
                "grupos": [{
                    "horario": "8:00 am",
                    "sessoes": [{
                        "nome": "Breakfast",
                        "inicio": "8:00 am",
                        "termino": "9:00 am",
                        "local": "Main hallway",
                        "tag": "Food",
                        "id": "1"
                    }]
                }, {
                    "horario": "9:00 am",
                    "sessoes": [{
                        "nome": "Introduction to Appcamp.io",
                        "local": "Room 2203",
                        "descricao": "Descrição",
                        "palestrantes": ["Ellie Elephant"],
                        "inicio": "9:15 am",
                        "termino": "9:30 am",
                        "tag": "Ionic",
                        "id": "2"
                    }, {
                        "nome": "Getting started with Ionic",
                        "local": "Room 2202",
                        "descricao": "Descrição",
                        "palestrantes": ["Ted Turtle"],
                        "inicio": "9:30 am",
                        "termino": "9:45 am",
                        "tag": "Ionic",
                        "id": "3"
                    }]
                }]
            },
            {
                "dia": "3",
                "mes": "mar",
                "grupos": [{
                    "horario": "8:00 am",
                    "sessoes": [{
                        "nome": "Breakfast",
                        "inicio": "8:00 am",
                        "termino": "9:00 am",
                        "local": "Main hallway",
                        "tag": "Food",
                        "id": "1"
                    }]
                }, {
                    "horario": "9:00 am",
                    "sessoes": [{
                        "nome": "Introduction to Appcamp.io",
                        "local": "Room 2203",
                        "descricao": "Descrição",
                        "palestrantes": ["Ellie Elephant"],
                        "inicio": "9:15 am",
                        "termino": "9:30 am",
                        "tag": "Ionic",
                        "id": "2"
                    }, {
                        "nome": "Getting started with Ionic",
                        "local": "Room 2202",
                        "descricao": "Descrição",
                        "palestrantes": ["Ted Turtle"],
                        "inicio": "9:30 am",
                        "termino": "9:45 am",
                        "tag": "Ionic",
                        "id": "3"
                    }]
                }]
            },
            {
                "dia": "4",
                "mes": "mar",
                "grupos": [{
                    "horario": "8:00 am",
                    "sessoes": [{
                        "nome": "Breakfast",
                        "inicio": "8:00 am",
                        "termino": "9:00 am",
                        "local": "Main hallway",
                        "tag": "Food",
                        "id": "1"
                    }]
                }, {
                    "horario": "9:00 am",
                    "sessoes": [{
                        "nome": "Introduction to Appcamp.io",
                        "local": "Room 2203",
                        "descricao": "Descrição",
                        "palestrantes": ["Ellie Elephant"],
                        "inicio": "9:15 am",
                        "termino": "9:30 am",
                        "tag": "Ionic",
                        "id": "2"
                    }, {
                        "nome": "Getting started with Ionic",
                        "local": "Room 2202",
                        "descricao": "Descrição",
                        "palestrantes": ["Ted Turtle"],
                        "inicio": "9:30 am",
                        "termino": "9:45 am",
                        "tag": "Ionic",
                        "id": "3"
                    }]
                }]
            },
            {
                "dia": "5",
                "mes": "mar",
                "grupos": [
                    {
                        "horario": "8:00 am",
                        "sessoes": [{
                            "nome": "Breakfast",
                            "inicio": "8:00 am",
                            "termino": "9:00 am",
                            "local": "Main hallway",
                            "tag": "Food",
                            "id": "1"
                        }]
                    },
                    {
                        "horario": "9:00 am",
                        "sessoes": [{
                            "nome": "Introduction to Appcamp.io",
                            "local": "Room 2203",
                            "descricao": "Descrição",
                            "palestrantes": ["Ellie Elephant"],
                            "inicio": "9:15 am",
                            "termino": "9:30 am",
                            "tag": "Ionic",
                            "id": "2"
                        }, {
                            "nome": "Getting started with Ionic",
                            "local": "Room 2202",
                            "descricao": "Descrição",
                            "palestrantes": ["Ted Turtle"],
                            "inicio": "9:30 am",
                            "termino": "9:45 am",
                            "tag": "Ionic",
                            "id": "3"
                        }]
                    }]
            }
        ]
    }

    return jsonify(response), 200
