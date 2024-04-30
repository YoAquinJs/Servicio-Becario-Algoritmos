class HttpError extends Error {
    constructor(message) {
        super(message);

        if (Error.captureStackTrace)
            Error.captureStackTrace(this, MyCustomError);

        this.name = "HttpError";
        this.date = new Date();
    }
}

class ResponseFormatError extends Error {
    constructor(message) {
        super(message);

        if (Error.captureStackTrace)
            Error.captureStackTrace(this, MyCustomError);

        this.name = "ResponseFormatError";
        this.date = new Date();
    }
}
