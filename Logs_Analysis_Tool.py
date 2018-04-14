#! /usr/bin/env python
from invalidlog import daysDidMoreThan1Precent
from logs import get_alltime
from themostpopularauthors import mostPopularAuthors


def allAnswersForQuestions():
    first_quest = get_alltime()
    second_quest = mostPopularAuthors()
    third_quest = daysDidMoreThan1Precent()
    return first_quest, second_quest, third_quest


if __name__ == '__main__':
    allAnswersForQuestions()
