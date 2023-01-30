import pytest
from web.fakers import RandomApplicantFactory


@pytest.mark.parametrize('index', range(6))
def test_flow(site, index):
    index_page = site.index_page
    index_page.open()
    index_page.click_accept_cookies()
    index_page.footer.scroll_to_item_and_click('Careers')
    site.open_career_page.click_on_career_dialog_rnd()
    site.career_department_page.get_position_by_index(index)
    applicant = RandomApplicantFactory.create()
    site.career_applicant_page.applicant_form.fill_form(**applicant.dict)

