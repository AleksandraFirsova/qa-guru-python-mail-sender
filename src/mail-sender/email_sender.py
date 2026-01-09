import email_utils


def sender_email(recipient_list, subject, message, *, sender="default@study.com"):
    if not recipient_list:
        return []

    sender_result = email_utils.get_correct_email([sender])
    if not sender_result:
        return []
    sender = sender_result[0]

    recipient_list = email_utils.get_correct_email(recipient_list)
    if not recipient_list:
        return []

    if not email_utils.check_empty_fields(subject, message):
        return []

    filtered_recipients = []
    for r in recipient_list:
        if r != sender:
            filtered_recipients.append(r)

    if not filtered_recipients:
        return []

    recipient_list = filtered_recipients

    subject = email_utils.clean_body_text(subject)
    body = email_utils.clean_body_text(message)

    recipient_list = [email_utils.normalize_addresses(r) for r in recipient_list]
    sender = email_utils.normalize_addresses(sender)

    login, domain = email_utils.extract_login_domain(sender)
    masked_sender = email_utils.mask_sender_email(login, domain)

    result = []

    for recipient in recipient_list:

        email = email_utils.create_email(sender, recipient, subject, body)

        email = email_utils.add_send_date(email)

        email["masked_sender"] = masked_sender

        if len(email["body"]) > 10:
            email["short_body"] = email["body"][:10] + "..."
        else:
            email["short_body"] = email["body"]

        email["sent_text"] = email_utils.build_sent_text(email)

        result.append(email)

    return result
