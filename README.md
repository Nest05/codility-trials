# Codility Practice

1.  You are given a list of names of new employees in a company. You need to generate a company email address for each of them.
    The name of each person consists of two or three parts: a first name, an optional middle name, and a last name, separated by spaces. Each part can include only English letters (but the last name may additionally contain hyphens). The name of the company also consists only of English letters.
    Each address must use the format "FirstMiddleLast@Company.com" where
    First is the initial of the first name,
    Middle is the initial of the middle name (but only if the person has a middle name),
    Last is the last name, truncated to at most 8 initial letters,
    Company is the company name.
    The address should be in lower case and should not contain hyphens.
    Note that hyphens should be removed before truncating the last name.
    Additionally, if more than one person would have the same email address, differentiate their addresses by adding subsequent integers (starting from the second address and number 2) before the "@" sign. For example, if there are three people who would have the address "jd@company.com", they should be assigned addresses "jd@company.com", "jd2@company.com" and "jd3@company.com" respectively.
    Write a function:
    def solution(S, C)
    that, given a string S containing a list of names separated by the characters ", "
    (a comma followed by a space)
    and a string C specifying the name of the company, returns a string containing the list of email addresses separated by the characters ", " in the same order as they were in the input. Each entry on the list should be of the form "Name <Email>".
    For example, given C = "Example" and string S as follows:
    "John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker"
    the function should return:
    "John Doe <jdoe@example.com>, Peter Parker <pparker@example.com>, Mary Jane Watson-Parker <mjwatsonpa@example.com>, James Doe <jdoe2@example.com>, John Elvis Doe <jedoe@example.com>, Jane Doe <jdoe3@example.com>, Penny Parker <pparker2@example.com>".