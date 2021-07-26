Name:           python-sphobjinv
Version:        2.1.0
Release:        1
Summary:        Sphinx objects.inv inspection/manipulation tool

License:        MIT
URL:            https://github.com/bskinn/sphobjinv
Source0:        https://github.com/bskinn/sphobjinv/archive/refs/tags/v2.1.tar.gz
BuildArch:      noarch

%description
The syntax required for a functional Sphinx cross-reference is highly
non-obvious in many cases. Sometimes Sphinx can guess correctly what
you mean, but it’s pretty hit-or-miss. The best approach is to provide
Sphinx with a completely specified cross-reference, and that’s where
sphobjinv comes in.

%package -n     python3-sphobjinv
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-sphobjinv}

%description -n python3-sphobjinv
The syntax required for a functional Sphinx cross-reference is highly
non-obvious in many cases. Sometimes Sphinx can guess correctly what
you mean, but it’s pretty hit-or-miss. The best approach is to provide
Sphinx with a completely specified cross-reference, and that’s where
sphobjinv comes in.

%prep
%autosetup -n sphobjinv-2.1.0
rm -rf sphobjinv.egg-info
sed -i "s|\r||g" README.rst


%build
%py3_build

%install
%py3_install

%files -n python3-sphobjinv
%license LICENSE.txt
%doc README.rst
%{_bindir}/sphobjinv
%{python3_sitelib}/sphobjinv/
%{python3_sitelib}/sphobjinv-2.1.0-py*.egg-info/

%changelog
* Thu Jul 08 2021 xuyonghui <xuyonghui@kylinos.cn> - 2.1.0-1
- Package init
