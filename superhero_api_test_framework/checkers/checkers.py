from hamcrest import assert_that, is_, none, equal_to


def smoke_check(function_to_decorate):
    def a_wrapper_accepting_arguments(iterate):
        url_for_check = function_to_decorate(iterate)

        assert_that(url_for_check.raise_for_status(), is_(none()))
        assert_that(url_for_check.json().get('response'), is_(equal_to('success')))

        return function_to_decorate

    return a_wrapper_accepting_arguments
