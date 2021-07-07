import os
from collections import defaultdict

from airium import Airium


SELF_EVALUATION_QUESTIONS = [
    "I am an empathic person, e.g. I get sad or angry during dramatic scenes in movies.",
    "I can easily hear and identify how a person feels in a phone conversation. I don’t need to see them to recognize their emotions.",
    "I am musically trained, e.g. I can play a musical instrument.",
    "High audio quality in media is important to me, e.g. I own high-end speakers.",
    "I am good at predicting other people’s behavior , e.g. I know how my actions will make others feel."
]


def get_file_list():
    file_list = os.listdir('./out/samples')
    _files_by_sample_id = defaultdict(list)
    
    for file in file_list:
        _files_by_sample_id[file.split('_')[0]].append(file)
    return sorted(_files_by_sample_id.items())


def extract_file_identifier(file):
    return '_'.join([file.split('_')[0], file.split('_')[2], file.split('_')[3]])


def add_type_to_file_identifier(type, file):
    return '_'.join([file.split('_')[0], type, file.split('_')[1], file.split('_')[2]])


def generate_html():
    a = Airium()

    a('<!DOCTYPE html>')
    with a.html():
        with a.head():
            a.title(_t="Speech Evaluation")
            a.meta(name="viewport", content="width=device-width, initial-scale=1.0")
            a.link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css", rel="stylesheet", integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6", crossorigin="anonymous")
        with a.body():
            with a.div(klass="container pb-5 pt-5"):
                a.h1(_t="Emotional Speech Evaluation", klass="text-center text-success display-1 pt-5 pb-5")
                a.p(
                    _t="Thank you for your time and welcome to the subjective evaluation of our emotional speech samples!",
                    klass="pt-5"
                )
                a.p(
                    _t="""First, you will need to answer 5 questions about yourself to make us know you more.
                    Then you will hear overall 80 audio samples, for each of which you are invited to answer 5 questions.
                    If you are uncertain about an answer listen to the audio sample multiple times.
                    """
                )
                a.p(
                    _t="""It is highly recommended to wear headphones during the evaluation.
                    """
                )
                with a.p():
                    a.span(_t="""After you click ‘Submit’, all your answers will be recorded, and a CSV file will be
                    downloaded. Please send the CSV file to 
                    """)
                    a.a(
                        href="mailto:zijiang.yang@informatik.uni-augsburg.de?subject=Emotional Speech Evalution",
                        _t="zijiang.yang@informatik.uni-augsburg.de",
                        target="_blank",
                        rel="noopener noreferrer"
                    )
                    a.span(
                        _t=". Thanks for your help!"
                    )
                a.p(_t="Note: Please answer all questions. ‘Submit’ button will bring you back to the unfinished questions.")
                with a.form(klass="pt-5 pb-5", id="evaluation-form", action="#", onsubmit="return submitForm();"):
                    with a.div(klass="form-group col-md-4"):
                        a.label(_t="Name", for_="name-input")
                        a.input(id="name-input", klass="form-control", type="text", placeholder="Jane Smith", required=True)
                    with a.div(klass="form-group col-md-8"):
                        for index, question in enumerate(SELF_EVALUATION_QUESTIONS):
                            with a.div(klass="card mt-5"):
                                with a.div(klass="card-body"):
                                    a.p(_t=question, klass="pb-3")
                                    with a.div(klass="custom-control custom-radio form-check-inline"):
                                        a.input(type="radio", id=f"self-evaluation-{index}-1", name=f"self-evaluation-{index}", klass="custom-control-input", value=1, required=True)
                                        a.label(_t="1 — Strongly disagree", klass="custom-control-label", for_=f"self-evaluation-{index}-1")
                                    with a.div(klass="custom-control custom-radio form-check-inline"):
                                        a.input(type="radio", id=f"self-evaluation-{index}-2", name=f"self-evaluation-{index}", klass="custom-control-input", value=2)
                                        a.label(_t="2 — Disagree", klass="custom-control-label", for_=f"self-evaluation-{index}-2")
                                    with a.div(klass="custom-control custom-radio form-check-inline"):
                                        a.input(type="radio", id=f"self-evaluation-{index}-3", name=f"self-evaluation-{index}", klass="custom-control-input", value=3)
                                        a.label(_t="3 — Neutral", klass="custom-control-label", name=f"self-evaluation-{index}", for_=f"self-evaluation-{index}-3")
                                    with a.div(klass="custom-control custom-radio form-check-inline"):
                                        a.input(type="radio", id=f"self-evaluation-{index}-4", name=f"self-evaluation-{index}", klass="custom-control-input", value=4)
                                        a.label(_t="4 — Agree", klass="custom-control-label", for_=f"self-evaluation-{index}-4")
                                    with a.div(klass="custom-control custom-radio form-check-inline"):
                                        a.input(type="radio", id=f"self-evaluation-{index}-5", name=f"self-evaluation-{index}", klass="custom-control-input", value=5)
                                        a.label(_t="5 — Strongly agree", klass="custom-control-label", for_=f"self-evaluation-{index}-5")
                    a.h4(_t="Emotional Speech Evalution", klass="mt-5 pt-5 text-success")
                    for index, (_, files) in enumerate(get_file_list()):
                        if index % 2 == 1:
                            color_scheme = "bg-secondary bg-gradient text-white"
                        else:
                            color_scheme = "bg-light bg-gradient"
                        with a.div(klass=f"card mt-5 {color_scheme}"):
                            with a.div(klass="card-body"):
                                a.h5(klass="cart-title mb-5", _t=f"Sample {index + 1}")
                                with a.div(klass="row"):
                                    sorted_files = sorted(files)
                                    with a.div(klass="col-lg-4 align-self-center"):
                                        with a.div(klass="text-center"):
                                            a.h6(_t="X")
                                            a.audio(controls=True, src=f"samples/{sorted_files[2]}", klass='mb-5')
                                    with a.div(klass="col-lg-4 align-self-center"):
                                        with a.div(klass="text-center"):
                                            sorted_files = sorted(files)
                                            a.h6(_t="A")
                                            a.audio(controls=True, src=f"samples/{sorted_files[0]}", klass='mb-5')
                                    with a.div(klass="col-lg-4 align-self-center"):
                                        with a.div(klass="text-center"):
                                            sorted_files = sorted(files)
                                            a.h6(_t="B")
                                            a.audio(controls=True, src=f"samples/{sorted_files[1]}", klass="mb-5")
                                with a.div(klass="row"):
                                    with a.div(klass="align-self-center text-center"):
                                        with a.p(klass="pb-1"):
                                            a.span(_t="Which one of A and B is more similar to X in emotion expression?")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-1-{extract_file_identifier(files[0])}", name=f"tts-evaluation-{extract_file_identifier(files[0])}", klass="custom-control-input", value=1, required=True)
                                            a.label(_t="A", klass="custom-control-label", for_=f"tts-evaluation-1-{files[0].split('_')[2]}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-2-{extract_file_identifier(files[0])}", name=f"tts-evaluation-{extract_file_identifier(files[0])}", klass="custom-control-input", value=2)
                                            a.label(_t="B", klass="custom-control-label", for_=f"tts-evaluation-2-{extract_file_identifier(files[0])}")
                    with a.div(klass="from-group mt-5"):
                        a.label(_for="open-comments", _t="Please leave your general opinion about the speeches here. We are also happy to hear your valuable suggestions. Thanks!")
                        a.textarea(klass="form-control", id="open-comments", name="open-comments", placeholder="(Optional)", rows="3")
                    a.button(_t="Submit", type="submit", klass="btn btn-primary mt-5")
                    with a.p(klass="mt-3"):
                        a.span(_t="Please send the generated CSV file to ")
                        a.a(
                            href="mailto:zijiang.yang@informatik.uni-augsburg.de?subject=Emotional Speech Evalution",
                            _t="zijiang.yang@informatik.uni-augsburg.de",
                            target="_blank",
                            rel="noopener noreferrer"
                        )
                        a.span(
                            _t=". Thanks for your help!"
                        )
        with a.script():
            a(
                f'''
                function clearForm() {{
                    document.getElementById("evaluation-form").reset();
                }}

                function buildCsvRow(fileName, questionResponses) {{
                    return `${{fileName}};${{questionResponses[0]}};${{questionResponses[1]}};${{questionResponses[2]}};${{questionResponses[3]}};${{questionResponses[4]}}\\n`
                }}

                function getQuestionResponse(input_name) {{
                    return $(`input[name="${{input_name}}"]:checked`).val();
                }}

                function getSelfEvaluationResponses() {{
                    return [{",".join([f"getQuestionResponse('self-evaluation-{index}')" for index in range(5)])}];
                }}

                function getTtsEvaluationResponsesForFile(file_name) {{
                    return [{",".join([f"getQuestionResponse(`tts-evaluation-{index}-${{file_name}}`)" for index in range(1, 6)])}];
                }}

                function getOpenComments() {{
                    let comments = $(`textarea[name="open-comments"]`).val();
                    if ("" === comments) {{
                        return "(Optional)\\n";
                    }} else {{
                        return comments.replace(/\\r?\\n|\\r/g, " ") + "\\n";
                    }}
                }}

                function submitForm() {{
                    let name = $("#name-input").val();
                    let files = [{",".join([f"'{extract_file_identifier(files[0])}'" for _, files in get_file_list()])}];
                    let csv = "data:text/csv;charset=utf-8,";
                    csv += "filename;q1;q2;q3;q4;q5\\n";
                    csv += buildCsvRow("self_evaluation", getSelfEvaluationResponses());
                    for (let i = 0; i < files.length; i++) {{
                        csv += buildCsvRow(files[i], getTtsEvaluationResponsesForFile(files[i]));
                    }}
                    csv += getOpenComments();
                    let encodedUri = encodeURI(csv);
                    let downloadLink = document.createElement("a");
                    downloadLink.setAttribute("download", `${{name}}_results.csv`);
                    downloadLink.setAttribute("href", encodedUri);
                    document.body.appendChild(downloadLink);
                    downloadLink.click();
                    downloadLink.remove();
                    return false;
                }}
                '''
            )
        a.script(src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js", integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf", crossorigin="anonymous")
        a.script(src="https://code.jquery.com/jquery-3.6.0.min.js", integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=", crossorigin="anonymous")

    return str(a)


if __name__ == '__main__':
    html = generate_html()
    with open('./out/index.html', 'w') as file:
        file.write(html)
