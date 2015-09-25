(define (domain car_park)
  (:requirements :strips)
  (:predicates
   (is_car ?car)
   (is_board_pos ?pos)
   (is_H ?car)
   (is_V ?car)
   (is_empty ?pos)
   (loc_car ?car ?start_pos ?end_pos)
   (left_adj ?square_one ?square_two)
   (right_adj ?square_one ?square_two)
   (top_adj ?square_one ?square_two)
   (bottom_adj ?square_one ?square_two)
   )

  (:action move_left
  	:parameters (?car ?start_pos ?end_pos ?new_start_pos ?new_end_pos)
  	:precondition (and ((is_car ?car)
  						(is_H ?car)
  						(is_board_pos ?start_pos)
  						(is_board_pos ?end_pos)
  						(is_board_pos ?new_start_pos)
  						(is_board_pos ?new_end_pos)
  						(loc_car ?car ?start_pos ?end_pos)
  						(left_adj ?new_start_pos ?start_pos)
  						(left_adj ?new_end_pos ?end_pos)
  						(is_empty ?new_start_pos)
  						))
  	:effect (and((loc_car ?car ?new_start_pos ?new_end_pos)
  				 (not (is_empty ?new_start_pos))
  				 (is_empty ?end_pos)
  				))
  	)


  	(:action move_right
  	:parameters (?car ?start_pos ?end_pos ?new_start_pos ?new_end_pos)
  	:precondition (and ((is_car ?car)
  						(is_H ?car)
  						(is_board_pos ?start_pos)
  						(is_board_pos ?end_pos)
  						(is_board_pos ?new_start_pos)
  						(is_board_pos ?new_end_pos)
  						(loc_car ?car ?start_pos ?end_pos)
  						(right_adj ?new_start_pos ?start_pos)
  						(right_adj ?new_end_pos ?end_pos)
  						(is_empty ?new_end_pos)
  						))
  	:effect (and((loc_car ?car ?new_start_pos ?new_end_pos)
  				 (is_empty ?start_pos)
  				 (not (is_empty ?new_end_pos))
  				))
  	)

  	(:action move_up
  	:parameters (?car ?start_pos ?end_pos ?new_start_pos ?new_end_pos)
  	:precondition (and ((is_car ?car)
  						(is_V ?car)
  						(is_board_pos ?start_pos)
  						(is_board_pos ?end_pos)
  						(is_board_pos ?new_start_pos)
  						(is_board_pos ?new_end_pos)
  						(loc_car ?car ?start_pos ?end_pos)
  						(top_adj ?new_start_pos ?start_pos)
  						(top_adj ?new_end_pos ?end_pos)
  						(is_empty ?new_start_pos)
  						))
  	:effect (and((loc_car ?car ?new_start_pos ?new_end_pos)
  				 (is_empty ?end_pos)
  				 (not (is_empty ?new_start_pos))
  				))
  	)

  	(:action move_down
  	:parameters (?car ?start_pos ?end_pos ?new_start_pos ?new_end_pos)
  	:precondition (and ((is_car ?car)
  						(is_V ?car)
  						(is_board_pos ?start_pos)
  						(is_board_pos ?end_pos)
  						(is_board_pos ?new_start_pos)
  						(is_board_pos ?new_end_pos)
  						(loc_car ?car ?start_pos ?end_pos)
  						(bottom_adj ?new_start_pos ?start_pos)
  						(bottom_adj ?new_end_pos ?end_pos)
  						(is_empty ?new_end_pos)
  						))
  	:effect (and((loc_car ?car ?new_start_pos ?new_end_pos)
  				 (is_empty ?start_pos)
  				 (not (is_empty ?new_end_pos))
  				))
  	)
)