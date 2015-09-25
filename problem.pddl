(define (problem car_parking)
  (:domain car_park)
  (:objects sq-0 sq-1 sq-2 sq-3 sq-4 sq-5
  			sq-6 sq-7 sq-8 sq-9 sq-10 sq-11
  			sq-12 sq-13 sq-14 sq-15 sq-16 sq-17
  			sq-18 sq-19 sq-20 sq-21 sq-22 sq-23
  			sq-24 sq-25 sq-26 sq-27 sq-28 sq-29
  			sq-30 sq-31 sq-32 sq-33 sq-34 sq-35
  			car-1 car-2 car-3 car-4
  			car-5 car-6 car-7 car-8)
  (:init is_car(car-1) is_car(car-2) is_car(car-3) is_car(car-4)
  		 is_car(car-5) is_car(car-6) is_car(car-7) is_car(car-8)
  		 is_board_pos(sq-0) is_board_pos(sq-1) is_board_pos(sq-2) is_board_pos(sq-3) is_board_pos(sq-4) is_board_pos(sq-5)
  		 is_board_pos(sq-6) is_board_pos(sq-7) is_board_pos(sq-8) is_board_pos(sq-9) is_board_pos(sq-10) is_board_pos(sq-11)
  		 is_board_pos(sq-12) is_board_pos(sq-13) is_board_pos(sq-14) is_board_pos(sq-15) is_board_pos(sq-16) is_board_pos(sq-17)
  		 is_board_pos(sq-18) is_board_pos(sq-19) is_board_pos(sq-20) is_board_pos(sq-21) is_board_pos(sq-22) is_board_pos(sq-23)
  		 is_board_pos(sq-24) is_board_pos(sq-25) is_board_pos(sq-26) is_board_pos(sq-27) is_board_pos(sq-28) is_board_pos(sq-29)
  		 is_board_pos(sq-30) is_board_pos(sq-31) is_board_pos(sq-32) is_board_pos(sq-33) is_board_pos(sq-34) is_board_pos(sq-35)
       loc_car(car-1 sq-21 sq-23)
       is_empty(sq-0)
       left_adj(sq-0 sq-1)
       right_adj(sq-1 sq-0)
       top_adj(sq-0 sq-6)
       bottom_adj(sq-6 sq-0)
  		 )
)
(define (problem wumpus-b-1)
  (:domain wumpus-b)
  (:objects sq-1-1 sq-1-2 sq-1-3
	    sq-2-1 sq-2-2 sq-2-3
	    the-gold the-arrow
	    agent wumpus)
  (:init (adj sq-1-1 sq-1-2) (adj sq-1-2 sq-1-1)
	 (adj sq-1-2 sq-1-3) (adj sq-1-3 sq-1-2)
	 (adj sq-2-1 sq-2-2) (adj sq-2-2 sq-2-1)
	 (adj sq-2-2 sq-2-3) (adj sq-2-3 sq-2-2)
	 (adj sq-1-1 sq-2-1) (adj sq-2-1 sq-1-1)
	 (adj sq-1-2 sq-2-2) (adj sq-2-2 sq-1-2)
	 (adj sq-1-3 sq-2-3) (adj sq-2-3 sq-1-3)
	 (pit sq-1-2)
	 (at the-gold sq-1-3)
	 (is-gold the-gold)
	 (takeable the-gold)
	 (at agent sq-1-1)
	 (alive agent)
	 (have agent the-arrow)
	 (is-arrow the-arrow)
	 (takeable the-arrow)
	 (at wumpus sq-2-3)
	 (alive wumpus))
  (:goal (and (have agent the-gold)
              (at agent sq-1-1)
          ))
  )