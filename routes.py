from fastapi.responses import JSONResponse

def addition1(number1,number2):
    res = number1 + number2
    return JSONResponse(
        content={"success": True, "res": res},
        status_code=200,
    )

