
from datetime import datetime

class viewx:
    def __init__(self, value):
        self.value = value

    def viewthing(self):
        BLOCK_VIEW = {
                "title": {
                    "type": "plain_text",
                    "text": "TODO"
                },
                "submit": {
                    "type": "plain_text",
                    "text": "Submit"
                },
                "type": "modal",
                "callback_id": "todo_view",
                "blocks": [
                    {
                        "type": "input",
                        "block_id": "block_a",
                        "element": {
                            "type": "plain_text_input",
                            "multiline": True,
                            "action_id": "todo_input"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "ToDo/Việc cần làm",
                            "emoji": True
                        }
                    },
                    {
                        "type": "input",
                        "optional": True,
                        "block_id": "block_b",
                        "element": {
                            "type": "multi_users_select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select users",
                                "emoji": True
                            },
                            "action_id": "user_input"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Chọn người để giao việc/Assign to",
                            "emoji": True
                        }
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "Thêm tính năng/More options",
                                    "emoji": True
                                },
                                "value": "button",
                                "action_id": "more"
                            }
                        ]
                    }
                ]
            }
        return BLOCK_VIEW

    def extendviewthing(self):
        BLOCK_VIEW = {
                "title": {
                    "type": "plain_text",
                    "text": "TODO"
                },
                "submit": {
                    "type": "plain_text",
                    "text": "Submit"
                },
                "type": "modal",
                "callback_id": "todo_view",
                "blocks": [
                    {
                        "type": "input",
                        "block_id": "block_a",
                        "element": {
                            "type": "plain_text_input",
                            "multiline": True,
                            "action_id": "todo_input"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "ToDo/Việc cần làm",
                            "emoji": True
                        }
                    },
                    {
                        "type": "input",
                        "optional": True,
                        "block_id": "block_b",
                        "element": {
                            "type": "multi_users_select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select users",
                                "emoji": True
                            },
                            "action_id": "user_input"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Chọn người để giao việc/Assign to",
                            "emoji": True
                        }
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "checkboxes",
                                "options": [
                                    {
                                        "text": {
                                            "type": "mrkdwn",
                                            "text": "*Nhắc nhở hằng ngày/Recurring tasks* (optional)"
                                        },
                                        "value": "value-0"
                                    }
                                ],
                                "action_id": "ticked"
                            }
                        ]
                    },
                    {
                        "type": "input",
                        "optional": True,
                        "block_id": "block_d",
                        "element": {
                            "type": "datepicker",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select a date",
                                "emoji": True
                            },
                            "action_id": "pick_date"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Chọn ngày/Datepicker",
                            "emoji": True
                        }
                    },
                    {
                        "type": "input",
                        "optional": True,
                        "block_id": "block_e",
                        "element": {
                            "type": "timepicker",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Có thể tự điền giờ/Type in time",
                                "emoji": True
                            },
                            "action_id": "timepicker"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Chọn giờ/Timepicker",
                            "emoji": True
                        }
                    }
                ]
            }
        return BLOCK_VIEW

    def extendviewthing_every(self):
        BLOCK_VIEW = {
                "title": {
                    "type": "plain_text",
                    "text": "TODO EVERYDAY"
                },
                "submit": {
                    "type": "plain_text",
                    "text": "Submit"
                },
                "type": "modal",
                "callback_id": "todo_view",
                "blocks": [
                    {
                        "type": "input",
                        "block_id": "block_a",
                        "element": {
                            "type": "plain_text_input",
                            "multiline": True,
                            "action_id": "todo_input"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "ToDo/Việc cần làm",
                            "emoji": True
                        }
                    },
                    {
                        "type": "input",
                        "optional": True,
                        "block_id": "block_b",
                        "element": {
                            "type": "multi_users_select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select users",
                                "emoji": True
                            },
                            "action_id": "user_input"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Chọn người để giao việc/Assign to",
                            "emoji": True
                        }
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "checkboxes",
                                "initial_options": [
                                    {
                                        "text": {
                                            "type": "mrkdwn",
                                            "text": "*Nhắc nhở hằng ngày/Recurring tasks* (optional)"
                                        },
                                        "value": "value-0"
                                    }
                                ],
                                "options": [
                                    {
                                        "text": {
                                            "type": "mrkdwn",
                                            "text": "*Nhắc nhở hằng ngày/Recurring tasks* (optional)"
                                        },
                                        "value": "value-0"
                                    }
                                ],
                                "action_id": "ticked_back"
                            }
                        ]
                    },
                    {
                        "type": "input",
                        "optional": True,
                        "block_id": "block_g",
                        "element": {
                            "type": "static_select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select an item",
                                "emoji": True
                            },
                            "options": [
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Hằng ngày/Everyday",
                                        "emoji": True
                                    },
                                    "value": "every"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Các thứ hai/Every monday",
                                        "emoji": True
                                    },
                                    "value": "mon"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Các thứ ba/Every tuesday",
                                        "emoji": True
                                    },
                                    "value": "tue"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Các thứ tư/Every wednesday",
                                        "emoji": True
                                    },
                                    "value": "wed"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Các thứ năm/Every thursday",
                                        "emoji": True
                                    },
                                    "value": "thu"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Các thứ sáu/Every friday",
                                        "emoji": True
                                    },
                                    "value": "fri"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Các thứ bảy/Every saturday",
                                        "emoji": True
                                    },
                                    "value": "sat"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Các chủ nhật/Every sunday",
                                        "emoji": True
                                    },
                                    "value": "sun"
                                }
                            ],
                            "action_id": "pickday"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Chọn ngày/Datepicker",
                            "emoji": True
                        }
                    },
                    {
                        "type": "input",
                        "optional": True,
                        "block_id": "block_e",
                        "element": {
                            "type": "timepicker",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Có thể tự điền giờ/Type in time",
                                "emoji": True
                            },
                            "action_id": "timepicker"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Chọn giờ/Timepicker",
                            "emoji": True
                        }
                    }
                ]
            }
        return BLOCK_VIEW


    def viewthingedit(self):
        BLOCK_VIEW = {
                "title": {
                    "type": "plain_text",
                    "text": "TODO EDIT"
                },
                "submit": {
                    "type": "plain_text",
                    "text": "Submit"
                },
                "type": "modal",
                "callback_id": "todo_view_edit",
                "blocks": [
                    {
                        "type": "input",
                        "block_id": "block_a",
                        "element": {
                            "type": "plain_text_input",
                            "multiline": True,
                            "action_id": "todo_input",
                            "initial_value": f"{self.value}"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "ToDo/Việc cần làm",
                            "emoji": True
                        }
                    },
                    {
                        "type": "section",
                        "block_id": "block_b",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":grey_exclamation: Bạn chỉ có thể sửa nội dung/You can only edit the task description."
                        }
                    }
                ]
            }
        return BLOCK_VIEW



    BLOCK_HOME = [
        {
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Tạo công việc/Create task",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "add"
				}
			]
		},
        {
			"type": "actions",
			"elements": [
                {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select an item",
                        "emoji": True
                    },
                    "initial_option": {
                        "text": {
                            "type": "plain_text",
                            "text": "Việc đang làm/Ongoing tasks",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Việc đang làm/Ongoing tasks",
                                "emoji": True
                            },
                            "value": "value-0"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Việc đã hoàn thành/Completed tasks",
                                "emoji": True
                            },
                            "value": "value-1"
                        }
                    ],
                    "action_id": "task_choose"
                }
			]
		},
        {
            "type": "divider"
        }
    ]

    BLOCK_HOME_DONE = [
        {
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Tạo công việc/Create task",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "add"
				}
			]
		},
        {
			"type": "actions",
			"elements": [
                {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select an item",
                        "emoji": True
                    },
                    "initial_option": {
                        "text": {
                            "type": "plain_text",
                            "text": "Việc đã hoàn thành/Completed tasks",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Việc đang làm/Ongoing tasks",
                                "emoji": True
                            },
                            "value": "value-0"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Việc đã hoàn thành/Completed tasks",
                                "emoji": True
                            },
                            "value": "value-1"
                        }
                    ],
                    "action_id": "task_choose"
                }
			]
		},
        {
            "type": "divider"
        }
    ]

    ACCESSORY = {
        "type": "overflow",
        "options": [
            {
                "text": {
                    "type": "plain_text",
                    "text": ":white_check_mark: Đã hoàn thành/Completed",
                    "emoji": True
                },
                "value": "value-0"
            },
            {
                "text": {
                    "type": "plain_text",
                    "text": ":pencil2: Sửa/Edit",
                    "emoji": True
                },
                "value": "value-1"
            },
            {
                "text": {
                    "type": "plain_text",
                    "text": ":x: Xóa/Delete",
                    "emoji": True
                },
                "value": "value-2"
            }
        ],
        "action_id": "overflow"
    }

    ACCESSORY_NEW = {
        "type": "overflow",
        "options": [
            {
                "text": {
                    "type": "plain_text",
                    "text": ":repeat: Chưa hoàn thành/Incomplete",
                    "emoji": True
                },
                "value": "value-3"
            },
            {
                "text": {
                    "type": "plain_text",
                    "text": ":x: Xóa/Delete",
                    "emoji": True
                },
                "value": "value-4"
            }
        ],
        "action_id": "overflow_new"
    }
