function random_walk(n) result(distance)
    implicit none

    integer, intent(in) :: n
    integer :: i, x, y, direction
    real(8) :: r, distance

    x = 0
    y = 0

    do i = 1, n
        ! random_number returns a value in the interval [0, 1).
        call random_number(r)
        direction = int(4.0d0 * r)

        select case (direction)
            case (0)
                x = x + 1
            case (1)
                x = x - 1
            case (2)
                y = y + 1
            case (3)
                y = y - 1
        end select
    end do

    distance = sqrt(real(x, 8)**2 + real(y, 8)**2)
end function random_walk
