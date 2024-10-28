; Auto-generated. Do not edit!


(cl:in-package first_coursework-msg)


;//! \htmlinclude Intention.msg.html

(cl:defclass <Intention> (roslisp-msg-protocol:ros-message)
  ((state
    :reader state
    :initarg :state
    :type cl:string
    :initform "")
   (distance
    :reader distance
    :initarg :distance
    :type cl:float
    :initform 0.0))
)

(cl:defclass Intention (<Intention>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Intention>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Intention)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name first_coursework-msg:<Intention> is deprecated: use first_coursework-msg:Intention instead.")))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <Intention>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader first_coursework-msg:state-val is deprecated.  Use first_coursework-msg:state instead.")
  (state m))

(cl:ensure-generic-function 'distance-val :lambda-list '(m))
(cl:defmethod distance-val ((m <Intention>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader first_coursework-msg:distance-val is deprecated.  Use first_coursework-msg:distance instead.")
  (distance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Intention>) ostream)
  "Serializes a message object of type '<Intention>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Intention>) istream)
  "Deserializes a message object of type '<Intention>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distance) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Intention>)))
  "Returns string type for a message object of type '<Intention>"
  "first_coursework/Intention")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Intention)))
  "Returns string type for a message object of type 'Intention"
  "first_coursework/Intention")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Intention>)))
  "Returns md5sum for a message object of type '<Intention>"
  "24590d8657c7ac106e9b50d9c4efeb47")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Intention)))
  "Returns md5sum for a message object of type 'Intention"
  "24590d8657c7ac106e9b50d9c4efeb47")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Intention>)))
  "Returns full string definition for message of type '<Intention>"
  (cl:format cl:nil "string state~%float32 distance~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Intention)))
  "Returns full string definition for message of type 'Intention"
  (cl:format cl:nil "string state~%float32 distance~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Intention>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'state))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Intention>))
  "Converts a ROS message object to a list"
  (cl:list 'Intention
    (cl:cons ':state (state msg))
    (cl:cons ':distance (distance msg))
))
