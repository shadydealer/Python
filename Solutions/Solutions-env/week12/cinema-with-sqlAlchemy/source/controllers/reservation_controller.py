from source.models.models import (Reservation,
                                  Projection,
                                  Session)
from source.controllers.user_controller import UserController

MAX_ROW_SIZE = 10
MAX_COL_SIZE = 10


class ReservationController:
    session = Session()

    @staticmethod
    def __validate_projection_id(*, projectionID):
        """
            Checks if the passed i projectionID is in the database.

            @param values projectionID - id of the projection we're validating.

            @param types projectionID - integer. 
        """
        projection = ReservationController.session.query(
            Projection).filter(Projection.id == projectionID).first()
        if projection == None:
            return False
        return True

    @staticmethod
    def __valid_row(*, row):
        """
            Checks if the passed in row is valid.

            @param values row - number of the row we're checking.

            @param types row - integer. 
        """
        return True if row <= MAX_ROW_SIZE and row >= 1 else False

    @staticmethod
    def __valid_col(*, col):
        """
            Checks if the passed in col is valid.

            @param values col - number of the col we're checking.

            @param types col - integer. 
        """
        return True if col <= MAX_COL_SIZE and col >= 1 else False

    @staticmethod
    def __validate_seat(*, projectionID, row, col):
        """
            Checks if the passed in row and col values
            are valid and haven't been reserved by somebody else.


            @param values projectionID - id of the projection.
            @param values row - number of the row we're checking.
            @param values col - number of the col we're checking.

            @param types projectionID - integer.
            @param types row - integer.
            @param types col - integer.
        """

        if ReservationController.__valid_row(row=row):
            if ReservationController.__valid_col(col=col):
                reservation = ReservationController.fetch_reservation(
                    projectionID=projectionID,
                    row=row,
                    col=col)
                if reservation == None:
                    return True
                else:
                    print("We're sorry but the seat is taken.")
            else:
                print("Col value must be between 1 and {}".format(MAX_COL_SIZE))
        else:
            print("Row value must be between 1 and {}".format(MAX_ROW_SIZE))
        return False

    @staticmethod
    def __fetch_reservation_by_id(*, reservationID):
        """
            Fetches a reservation row from the database
            by given reservation id.

            @param values reservationID - id of the reservation.

            @param types reservationID- integer.

            @return type:
                Reservation object if the there's a row with given id in the database.
                None otherwise.
        """

        return ReservationController.session.query(Reservation).filter(Reservation.id == reservationID)

    @staticmethod
    def fetch_reservation(*, projectionID, row, col):
        """
            Fetches a projection row from the database by given values.

            @param values projectionID - id of the projection.
            @param values row - reserved row coordinate.
            @param values col - reserved col coordinate.

            @param types projectionID -integer.
            @param types row - integer.
            @param types col - integer.

            @return type:
                Reservation object if there's a row with these values.
                None otherwise.
        """
        return ReservationController.session.query(Reservation).filter(
            Reservation.projection_id == projectionID,
            Reservation.row == row,
            Reservation.col == col
        ).first()

    @staticmethod
    def make_reservation(*, user, projectionID, row, col):
        """
            Adds a reservation entry to the database.

            @param values user - user that's going to be making the reservation.
            @param values projection_id - id of the projection.
            @param values row - row in the cinema.
            @param values col - col in the cinema.

            @param types user- User object.
            @param types projection_id- integer.
            @param types row- integer.
            @param types col- integer. 
        """
        if (ReservationController.__validate_projection_id(projectionID=projectionID) and
                ReservationController.__validate_seat(projectionID=projectionID, row=row, col=col)):
            user.reservations.append(Reservation(
                projection_id=projectionID,
                row=row,
                col=col
            ))
            print("Successfully made a reservation.")
        
    @staticmethod
    def cancel_reservation(*, user, reservationID):
        """
            Removes a reservation entry from the database
            if the passed in user is the same one that made the reservation.

            @param values user - user that's canceling the reservation.
            @param values reservationID - id of the reservation that we're removing.

            @param type user - User object.
            @param type reservationID - integer.
        """
        reservation = ReservationController.__fetch_reservation_by_id(
            reservationID=reservationID)
        if reservation != None:
            if reservation.user_id == user.id:
                ReservationController.session.delete(reservation)
                print("Successfully removed reservation {} from the database.".format(
                    reservationID))
            else:
                print("You do not have permission to remove somebody elses reservation.")
        else:
            print("No such reservation exist in the database.")
