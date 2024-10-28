;; Auto-generated. Do not edit!


(when (boundp 'first_coursework::Intention)
  (if (not (find-package "FIRST_COURSEWORK"))
    (make-package "FIRST_COURSEWORK"))
  (shadow 'Intention (find-package "FIRST_COURSEWORK")))
(unless (find-package "FIRST_COURSEWORK::INTENTION")
  (make-package "FIRST_COURSEWORK::INTENTION"))

(in-package "ROS")
;;//! \htmlinclude Intention.msg.html


(defclass first_coursework::Intention
  :super ros::object
  :slots (_state _distance ))

(defmethod first_coursework::Intention
  (:init
   (&key
    ((:state __state) "")
    ((:distance __distance) 0.0)
    )
   (send-super :init)
   (setq _state (string __state))
   (setq _distance (float __distance))
   self)
  (:state
   (&optional __state)
   (if __state (setq _state __state)) _state)
  (:distance
   (&optional __distance)
   (if __distance (setq _distance __distance)) _distance)
  (:serialization-length
   ()
   (+
    ;; string _state
    4 (length _state)
    ;; float32 _distance
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _state
       (write-long (length _state) s) (princ _state s)
     ;; float32 _distance
       (sys::poke _distance (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _state
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _distance
     (setq _distance (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get first_coursework::Intention :md5sum-) "24590d8657c7ac106e9b50d9c4efeb47")
(setf (get first_coursework::Intention :datatype-) "first_coursework/Intention")
(setf (get first_coursework::Intention :definition-)
      "string state
float32 distance
")



(provide :first_coursework/Intention "24590d8657c7ac106e9b50d9c4efeb47")


