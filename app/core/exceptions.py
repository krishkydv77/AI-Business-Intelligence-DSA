from fastapi import HTTPException, status

class DatasetNotFoundError(HTTPException):
    def __init__(self, dataset_id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Dataset with ID '{dataset_id}' was not found."
        )

class InvalidCSVError(HTTPException):
    def __init__(self, message: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid CSV file: {message}"
        )

class MissingColumnError(HTTPException):
    def __init__(self, column_name: str):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Required column '{column_name}' is missing in the dataset."
        )