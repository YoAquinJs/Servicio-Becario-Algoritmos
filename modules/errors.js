export class HttpError extends Error {
    constructor(statusCode, detail) {
        super(`Failed request with code ${statusCode}`);

        if (Error.captureStackTrace)
            Error.captureStackTrace(this, HttpError);

        this.name = "HttpError";
        this.statusCode = statusCode;
        this.detail = detail;
        this.date = new Date();
    }
}

export class ResponseFormatError extends Error {
    constructor(message) {
        super(message);

        if (Error.captureStackTrace)
            Error.captureStackTrace(this, ResponseFormatError);

        this.name = "ResponseFormatError";
        this.date = new Date();
    }
}
