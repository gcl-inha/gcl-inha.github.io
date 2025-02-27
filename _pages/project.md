---
layout: page
permalink: /project
title: Projects
description: 
nav: true
nav_order: 5
---

<style>
.project {
    display: flex;
    align-items: center; /* 세로 중앙 정렬 */
    gap: 30px; /* 이미지와 텍스트 간격 */
    margin-bottom: 30px; /* 프로젝트 간 간격 */
}

.project img {
    min-width: 250px;
    width: 250px; /* 이미지 크기 */
    height: 120px;
    border-radius: 4px; /* 모서리 둥글게 (선택사항) */
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.2);
}

/* 특정 해상도 이하일 때 (예: 768px 이하) */
@media (max-width: 768px) {
    .project {
        flex-direction: column; /* 이미지가 위로 가도록 변경 */
        align-items: flex-start; /* 텍스트를 왼쪽 정렬 */
    }

    .project img {
        width: 100%; /* 이미지가 부모 요소 너비에 맞게 */
        max-width: 250px; /* 최대 크기 제한 */
        height: auto; /* 높이 자동 조정 */
    }
}

</style>

### Current Projects
<div class="project" style="margin-top: 30px;">
    <img src="assets/funds/genai.png">
    <div>
        <strong>[참여] 산업융합형 멀티모달 생성인공지능 인재양성사업</strong><br>
        Developing Multimodal Generative AI Talent for Industrial Convergence<br>
        (2024.04 ~ 2027.12)<br>
        Funded by Institute for Information & communications Technology Promotion (IITP) (정보통신기획평가원 생성AI 선도인재양성사업)
    </div>
</div>

<div class="project">
    <img src="assets/funds/bk21.jpg">
    <div>
        <strong>[참여] BK21 산업융합형 차세대 인공지능 혁신인재 교육연구단</strong><br>
        (2020.09 ~ 2027.08)<br>
        Funded by National Research Foundation (교육부 4단계 BK21 사업)
    </div>
</div>

<div class="project">
    <img src="assets/funds/ai_center.png">
    <div>
        <strong>[참여] 인공지능융합연구센터 / 인공지능융합혁신대학원사업</strong><br>
        Artificial Intelligence Convergence Research Center<br>
        (2020.04 ~ 2025.12)<br>
        Funded by Institute for Information & communications Technology Promotion (IITP) (정보통신기획평가원 인공지능융합연구센터/인공지능융합혁신대학원 지원사업)
    </div>
</div>
