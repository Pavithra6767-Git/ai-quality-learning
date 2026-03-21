{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMjEZQ0Mw6TOzNP8BH44PW0",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Pavithra6767-Git/ai-quality-learning/blob/main/day8_practice.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WSlcCQ7DErnC",
        "outputId": "f1ea291b-c5cb-484e-f06b-3c0d46f934ea"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "AI Test Results Summary\n",
            "Total tests: 6\n",
            "Passed: 4 (67%)\n",
            "Failed: 2 (33%)\n"
          ]
        }
      ],
      "source": [
        "test_results = [\"pass\", \"pass\", \"fail\", \"pass\", \"fail\", \"pass\"]\n",
        "total = len(test_results)\n",
        "passed = test_results.count(\"pass\")\n",
        "failed = test_results.count(\"fail\")\n",
        "\n",
        "print(f\"AI Test Results Summary\")\n",
        "print(f\"Total tests: {total}\")\n",
        "print(f\"Passed: {passed} ({round(passed/total*100)}%)\")\n",
        "print(f\"Failed: {failed} ({round(failed/total*100)}%)\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Variables\n",
        "tester_name = \"Pavithra\"\n",
        "test_date = 2026\n",
        "total_tests = 6\n",
        "\n",
        "#List of test results\n",
        "results = [\"pass\", \"fail\", \"pass\", \"pass\", \"pass\", \"pass\"]\n",
        "\n",
        "#Dictionary (AI model being tested)\n",
        "ai_model = {\n",
        "    \"name\" : \"Claude\",\n",
        "    \"version\" : 3.5,\n",
        "    \"test_type\" : \"Hallucination Detection\",\n",
        "    \"tester\" : \"Pavithra\"\n",
        "}\n",
        "\n",
        "#Calculate summary\n",
        "passed = results.count(\"pass\")\n",
        "failed = results.count(\"fail\")\n",
        "pass_rate = round((passed/total_tests)*100)\n",
        "\n",
        "#Print report\n",
        "print(\"=\" * 40)\n",
        "print(\"AI TEST RESULTS SUMMARY\")\n",
        "print(\"=\" * 40)\n",
        "print(f\"Model: {ai_model['name']} {ai_model['version']}\")\n",
        "print(f\"Test Type: {ai_model['test_type']}\")\n",
        "print(f\"Tester: {ai_model['tester']}\")\n",
        "print(f\"Date: {test_date}\")\n",
        "print(\"-\" * 40)\n",
        "print(f\"Total Tests: {total_tests}\")\n",
        "print(f\"Passed: {passed}\")\n",
        "print(f\"Failed: {failed}\")\n",
        "print(f\"Pass Rate: {pass_rate}%\")\n",
        "print(f\"Test Status: {'PASS' if pass_rate >= 70 else 'FAIL'}\")"
      ],
      "metadata": {
        "id": "GQ8L_YoJEvdF",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0a2582f9-4d6a-46da-d91e-92ee6d769077"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "========================================\n",
            "AI TEST RESULTS SUMMARY\n",
            "========================================\n",
            "Model: Claude 3.5\n",
            "Test Type: Hallucination Detection\n",
            "Tester: Pavithra\n",
            "Date: 2026\n",
            "----------------------------------------\n",
            "Total Tests: 6\n",
            "Passed: 5\n",
            "Failed: 1\n",
            "Pass Rate: 83%\n",
            "Test Status: PASS\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "CqZxk-KkGhBf"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}